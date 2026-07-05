# Daily Contribution Plan

**Goal:** Daily GitHub submissions + Zindi challenge progress

## Zindi WAXAL ASR Challenge (Jul 5 - Aug 2, 2026)

| Day | Date | Task | Deliverable |
|-----|------|------|-------------|
| 1 | Jul 5 | Setup project, baseline Whisper notebook | Repo structure, starter notebook |
| 2 | Jul 6 | Download WAXAL data, run baseline on subset | First Colab run results |
| 3 | Jul 7 | EDA: analyze language distribution, audio stats | EDA notebook + visualizations |
| 4 | Jul 8 | Fine-tune Whisper-small on Lingala | Model checkpoint |
| 5 | Jul 9 | Fine-tune Whisper-small on Shona | Model checkpoint |
| 6 | Jul 10 | Fine-tune Whisper-small on Luganda | Model checkpoint |
| 7 | Jul 11 | Multilingual training - all 3 languages | Combined model |
| 8 | Jul 12 | Hyperparameter tuning (LR, batch, epochs) | Optimized config |
| 9 | Jul 13 | Data augmentation: speed perturbation, noise | Augmented pipeline |
| 10 | Jul 14 | Language-specific decoding strategies | Improved WER/CER |
| 11 | Jul 15 | First Zindi submission | submission_1.csv |
| 12 | Jul 16 | Analyze leaderboard feedback | Improvement plan |
| 13 | Jul 17 | Try Whisper-medium (if VRAM allows) | model checkpoint |
| 14 | Jul 18 | Ensemble experiments (small + medium) | ensemble results |
| 15 | Jul 19 | Language ID + specialized models per language | per-lang models |
| 16 | Jul 20 | Second Zindi submission | submission_2.csv |
| 17 | Jul 21 | Iterate based on public LB score | refinements |
| 18 | Jul 22 | External data: research other African ASR datasets | dataset list |
| 19 | Jul 23 | Third Zindi submission | submission_3.csv |
| 20 | Jul 24 | Self-training / pseudo-labeling on unlabeled data | semi-supervised pipeline |
| 21 | Jul 25 | Fourth Zindi submission | submission_4.csv |
| 22 | Jul 26 | Phase 2 prep: robustness, noise handling | robust pipeline |
| 23 | Jul 27 | Fifth Zindi submission | submission_5.csv |
| 24 | Jul 28 | Model ensembling & blending | ensemble model |
| 25 | Jul 29 | Sixth Zindi submission + select top 2 | submission_6.csv |
| 26 | Jul 30 | Phase 2: prepare for unseen test set | phase2 ready |
| 27 | Jul 31 | Phase 2: run on new data | phase2 predictions |
| 28 | Aug 1 | Final tuning, select best 2 submissions | final submissions |
| 29 | Aug 2 | Challenge closes, submit final | - |

## Electronics / PCB Projects (interleaved)

| Day | Project | Description | Tools |
|-----|---------|-------------|-------|
| 1 | ESP32 Soil Sensor PCB | Design custom PCB for existing sensor | KiCad / EasyEDA |
| 2 | Audio Pre-amp for ASR | Microphone pre-amp circuit (tied to challenge) | KiCad |
| 3 | Smart Farm Valve Controller PCB | Motorized valve driver board | KiCad |
| 4 | IoT Weather Station | ESP32 + BME280 + solar | KiCad |
| 5 | USB-C Power Supply | 5V/3A buck converter PCB | KiCad |
| 6 | LoRa Node PCB | Long-range sensor node | KiCad |

## GitHub Repos Structure

1. **SMART-FARM** (existing) - smart-farm-api
2. **zindi-waxal-asr** (new) - ASR challenge code
3. **electronics-projects** (new) - KiCad PCB designs, schematics
4. **alx-data-science** (optional) - ALX/Data science notebooks
