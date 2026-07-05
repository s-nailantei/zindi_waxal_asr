import torch
import numpy as np
from datasets import load_dataset, Audio, concatenate_datasets, DatasetDict
from transformers import (
    WhisperFeatureExtractor, WhisperTokenizer, WhisperProcessor,
    WhisperForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer
)
from evaluate import load as load_metric
import pandas as pd
import random
import os

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

class WaxalASR:
    def __init__(self, model_name='openai/whisper-small', target_languages=None):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model_name = model_name
        self.target_languages = target_languages or ['lin', 'sna', 'lug']
        self.processor = None
        self.model = None
        set_seed()

    def load_data(self, subset=None):
        configs = [f'{lang}_asr' for lang in self.target_languages]
        all_splits = {'train': [], 'validation': [], 'test': []}
        for config in configs:
            ds = load_dataset('google/WaxalNLP', config, trust_remote_code=True)
            for split in ['train', 'validation', 'test']:
                all_splits[split].append(ds[split])
        combined = DatasetDict({
            split: concatenate_datasets(datasets) for split, datasets in all_splits.items()
        })
        combined = combined.cast_column('audio', Audio(sampling_rate=16000))
        if subset:
            for split in combined:
                n = min(subset, len(combined[split]))
                combined[split] = combined[split].shuffle(seed=42).select(range(n))
        return combined

    def load_model(self):
        self.processor = WhisperProcessor.from_pretrained(
            self.model_name, language='en', task='transcribe'
        )
        self.model = WhisperForConditionalGeneration.from_pretrained(self.model_name)
        self.model.config.forced_decoder_ids = None
        self.model.config.suppress_tokens = []
        self.model.to(self.device)
        return self.model

    def prepare_dataset(self, batch):
        audio = batch['audio']
        batch['input_features'] = self.processor.feature_extractor(
            audio['array'], sampling_rate=audio['sampling_rate']
        ).input_features[0]
        batch['labels'] = self.processor.tokenizer(batch['transcription']).input_ids
        return batch

    def compute_metrics(self, pred):
        tokenizer = self.processor.tokenizer
        pred_ids = pred.predictions
        label_ids = pred.label_ids
        label_ids[label_ids == -100] = tokenizer.pad_token_id
        pred_str = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)
        label_str = tokenizer.batch_decode(label_ids, skip_special_tokens=True)
        wer = load_metric('wer').compute(predictions=pred_str, references=label_str)
        cer = load_metric('cer').compute(predictions=pred_str, references=label_str)
        return {'wer': wer, 'cer': cer, 'combined': 0.5 * wer + 0.5 * cer}

    def train(self, train_dataset, val_dataset, output_dir='./waxal-model', **kwargs):
        from transformers import Seq2SeqDataCollator
        collator = Seq2SeqDataCollator(processor=self.processor, model=self.model)

        args = Seq2SeqTrainingArguments(
            output_dir=output_dir,
            per_device_train_batch_size=kwargs.get('batch_size', 16),
            per_device_eval_batch_size=kwargs.get('batch_size', 16),
            learning_rate=kwargs.get('lr', 1e-5),
            warmup_steps=kwargs.get('warmup', 200),
            num_train_epochs=kwargs.get('epochs', 5),
            evaluation_strategy='steps',
            eval_steps=kwargs.get('eval_steps', 200),
            save_steps=kwargs.get('save_steps', 200),
            logging_steps=50,
            report_to=['none'],
            predict_with_generate=True,
            generation_max_length=225,
            fp16=True,
            save_total_limit=3,
            seed=42,
            data_seed=42,
            load_best_model_at_end=True,
            metric_for_best_model='combined',
            greater_is_better=False,
        )

        trainer = Seq2SeqTrainer(
            model=self.model, args=args,
            train_dataset=train_dataset, eval_dataset=val_dataset,
            data_collator=collator, compute_metrics=self.compute_metrics,
            tokenizer=self.processor.feature_extractor,
        )
        trainer.train()
        trainer.save_model(output_dir)
        return trainer

    def predict(self, dataset, output_file='submission.csv'):
        self.model.eval()
        def _transcribe(batch):
            audio = batch['audio']
            inputs = self.processor.feature_extractor(
                audio['array'], sampling_rate=audio['sampling_rate'],
                return_tensors='pt'
            ).input_features.to(self.device)
            with torch.no_grad():
                ids = self.model.generate(inputs)
            return {'prediction': self.processor.batch_decode(ids, skip_special_tokens=True)[0]}

        predictions = dataset.map(_transcribe)
        df = pd.DataFrame({'id': predictions['id'], 'transcription': predictions['prediction']})
        df.to_csv(output_file, index=False)
        return df

if __name__ == '__main__':
    asr = WaxalASR()
    data = asr.load_data(subset=500)
    asr.load_model()
    train_ds = data['train'].map(asr.prepare_dataset, remove_columns=[
        'audio', 'transcription', 'speaker_id', 'gender', 'id', 'language'
    ])
    val_ds = data['validation'].map(asr.prepare_dataset, remove_columns=[
        'audio', 'transcription', 'speaker_id', 'gender', 'id', 'language'
    ])
    asr.train(train_ds, val_ds, epochs=1)
    asr.predict(data['test'], '../submissions/pipeline_submission.csv')
