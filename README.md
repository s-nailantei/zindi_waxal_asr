# Google WAXAL ASR Challenge - Zindi

**Competition:** https://zindi.africa/competitions/google-waxal-asr-challenge

**Goal:** Build ASR models for African languages (Lingala, Shona, Luganda) using the WAXAL dataset.

## Project Structure

```
zindi_waxal_asr/
├── data/               # Competition CSV files (download from Zindi)
│   ├── Train.csv       # Training metadata
│   ├── Test.csv        # Test metadata
│   └── SampleSubmission.csv
├── notebooks/          # Jupyter/Colab notebooks
├── src/                # Python source code
└── submissions/        # Generated submission files
```

## Setup

1. Download data files from Zindi competition page → `data/`
2. Run notebooks in Google Colab with GPU runtime
3. Submit predictions on Zindi

## Rules Compliance

- Open-source tools only (HuggingFace, PyTorch, etc.)
- No AutoML
- Max 5 submissions/day
- Max 200 submissions total
- Code must be reproducible (set seeds)
- Top 10 must submit code within 48h
