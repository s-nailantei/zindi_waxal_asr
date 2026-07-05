# Google WAXAL ASR Challenge — Complete Breakdown

## What This Project Is

An Automatic Speech Recognition (ASR) competition where we build models that convert African language speech audio into text. The focus languages are **Lingala, Shona, and Luganda** — spoken by ~100M+ people. We use the WAXAL dataset (~1,250 hours of natural speech across 19 African languages) from HuggingFace.

**Data files we have:**
- `Train.csv` — 39,013 rows: `id, transcription, language, original_split`
- `Test.csv` — 4,253 rows: just `ID` (we predict transcriptions for these)
- `SampleSubmission.csv` — format: `ID, Target`

**Metric:** Combined = 0.5 × WER + 0.5 × CER

---

## 1. What We Did (Technical Summary)

| Step | What | Tools |
|------|------|-------|
| Data loading | Loaded WAXAL from HuggingFace for 3 target languages | `datasets`, HuggingFace Hub |
| EDA | Explored language distribution, audio durations, transcriptions | Pandas, `datasets` |
| Preprocessing | Resampled audio to 16kHz, extracted Mel spectrograms | Whisper feature extractor |
| Model | Fine-tuned Whisper-small (244M params) on multilingual data | HuggingFace Transformers |
| Evaluation | Computed WER + CER on validation set | `evaluate` (jiwer) |
| Submission | Generate predictions → CSV with ID + transcription | Pandas |

**Baseline notebook:** `01_waxal_baseline_whisper.ipynb` — ready to run in Colab

---

## 2. What a Data Scientist Should Know & Learn

### Core Concepts
- **ASR Pipeline:** Audio → Features → Acoustic Model → Language Model → Text
- **WER vs CER:** Word Error Rate (insertions/deletions/substitutions at word level) vs Character Error Rate (same at character level). CER is more forgiving for morphologically rich languages.
- **Transfer Learning:** Whisper was pretrained on 680k hours of multilingual audio — we fine-tune on target languages with limited data.
- **Data Augmentation:** Speed perturbation, SpecAugment, noise injection — critical when labeled data is limited.

### Practical Skills Being Built
| Skill | Application Here |
|-------|-----------------|
| HuggingFace ecosystem | Loading datasets, models, trainers |
| Audio preprocessing | Feature extraction, resampling, normalization |
| Seq2Seq modeling | Encoder-decoder architectures |
| Multilingual NLP | Handling code-switching, language identification |
| Evaluation design | WER/CER computation, metric selection |
| Colab/GPU workflow | Training on limited hardware, checkpointing |

### Key Challenges in African-language ASR
- **Orthographic variation:** Same word spelled differently across sources
- **Code-switching:** Speakers mix languages mid-sentence
- **Low-resource:** Despite WAXAL being large, per-language data is modest compared to English
- **Tonal languages:** Luganda is tonal — pitch changes meaning, which ASR systems often miss

---

## 3. What an Electronics & Computer Engineer Should Know

### Signal Processing Connection
ASR sits at the intersection of signal processing and ML. Key DSP concepts:

| DSP Concept | Role in ASR |
|-------------|-------------|
| Sampling rate | Audio resampled to 16kHz (standard for speech) |
| FFT / STFT | Short-Time Fourier Transform → spectrogram |
| Mel scale | Human-perceptual frequency scaling |
| Filter banks | Mel-frequency cepstral coefficients (MFCCs) |
| Anti-aliasing | Critical when resampling (Nyquist theorem) |

### Hardware Considerations
- **Microphone hardware:** MEMS mics (INMP441, SPH0645) → I2S interface → ESP32 → cloud ASR
- **Edge vs Cloud:** On-device ASR (ESP32-S3 with audio front-end) vs cloud API
- **Audio chain:** Mic → Pre-amp → ADC → DSP → Feature Extraction → Model Inference
- **Latency:** Real-time ASR needs <300ms end-to-end; affects hardware choices

### Embedded Systems Context
The electronics projects (audio pre-amp PCB, ESP32 sensor boards) directly complement this. An end-to-end speech system involves:
1. Hardware: Microphone array, pre-amp, ADC
2. Firmware: I2S audio capture, WiFi transmission
3. Backend: ASR model inference (cloud or edge)
4. Application: Voice-controlled IoT (e.g., smart farm)

---

## 4. What Any Engineer Should Learn (General Principles)

### System Design Thinking
```
[Audio Source] → [Sensor/Hardware] → [Signal Processing] → [ML Model] → [Output]
     ↓                    ↓                   ↓                  ↓            ↓
  Microphone           Pre-amp PCB         FFT/Mel            Whisper      Text
  (electronics)        (PCB design)        (DSP/embedded)     (ML/data)    (product)
```
Every layer affects the next. Noise from poor PCB layout → degraded ASR accuracy.

### Engineering Principles Demonstrated
| Principle | Example |
|-----------|---------|
| **Trade-offs** | Model size vs. accuracy vs. inference speed |
| **Reproducibility** | Fixed seeds, deterministic preprocessing |
| **Evaluation hygiene** | Separate train/val/test, no data leakage |
| **Incremental building** | Baseline → improve → iterate |
| **Documentation** | Clear code, version control, experiment tracking |

### Rules Compliance Mindset
- Competition rules are engineering constraints — treat them like a spec sheet
- Open-source only, no AutoML, max 5 submissions/day — these shape your solution architecture
- Code review at top 10 means your code must be clean and reproducible

---

## 5. Skills Growth Path — Leveling Up

### Current Level (You're Here)
Day 1: Baseline Whisper fine-tune on a subset, single notebook, Colab free tier

### Intermediate (Next 2 Weeks)
- Full dataset training
- Hyperparameter optimization (LR, batch size, warmup steps)
- Language-specific decoding strategies
- Data augmentation (SpecAugment, speed perturbation)
- Multiple submissions, leaderboard tracking

### Advanced (Weeks 3-4)
- Ensemble multiple models (Whisper-small + Whisper-medium)
- Self-training / pseudo-labeling on unlabeled WAXAL data
- Language identification + per-language specialist models
- Knowledge distillation (large model → small model)
- Phase 2: generalization test on unseen data

### Expert Level (Beyond Competition)
- Train from scratch on WAXAL (not just fine-tune)
- Custom Conformer or CTC architectures
- Deploy model as API (FastAPI, ONNX runtime)
- Edge deployment on ESP32-S3 with TensorFlow Lite
- Write a paper / blog post on findings

### Domain Mastery Roadmap
```
Data Science ←→ Electronics Engineering
     ↓                  ↓
   ML/DL              Embedded Systems
     ↓                  ↓
   NLP/Audio          PCB Design
     ↓                  ↓
   └────── MLOps + Hardware ──────┘
                 ↓
       Full-Stack AI Engineer
```

### Next Actions (Tomorrow — Day 2)
1. Run `01_waxal_baseline_whisper.ipynb` in Colab on a 500-sample subset
2. Note the WER/CER on validation set
3. Check if Colab free GPU handles it (T4 16GB VRAM)
4. If yes, run the full training notebook overnight
5. Make first Zindi submission
