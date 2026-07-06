# Daily Contribution Plan

**Goal:** Daily GitHub submissions + Zindi challenge progress
**Started:** Jul 5, 2026 | **Challenge closes:** Aug 2, 2026

## Day 1 — Jul 5 ✅ COMPLETED

| Task | Status | Notes |
|------|--------|-------|
| Research challenge rules & dataset | ✅ | WAXAL on HuggingFace, 3 languages |
| Download competition files from Zindi | ✅ | Train.csv (39k rows), Test.csv (4.2k), SampleSubmission |
| Create project structure | ✅ | `data/`, `notebooks/`, `src/`, `submissions/` |
| Baseline Whisper notebook | ✅ | `01_waxal_baseline_whisper.ipynb` |
| Full training notebook | ✅ | `02_waxal_full_training.ipynb` |
| Python pipeline module | ✅ | `src/asr_pipeline.py` |
| Comprehensive ASR breakdown | ✅ | `WAXAL_ASR_BREAKDOWN.md` |
| Electronics projects setup | ✅ | `electronics_projects/`, 8 project ideas |
| Electronics breakdown guide | ✅ | `BREAKDOWN.md` |
| Git init + first commit | ✅ | Ready for GitHub push |

## Day 2 — Jul 6

### ASR Challenge
- [ ] **YOU:** Run `03_gemma_submission.ipynb` in Colab (T4 GPU)
- [ ] **YOU:** Upload submission CSV to Zindi portal
- [ ] Tell me your leaderboard score (WER + CER)
- [ ] We iterate from there

### Soil Sensor PCB
- [ ] **YOU:** Open Altium → File → New → PCB Project → `ESP32_Soil_Sensor.PrjPcb`
- [ ] **YOU:** Create `Main.SchDoc`, add components from schematic plan
- [ ] Wire power section: USB → LDO → ESP32
- [ ] Run ERC, fix any errors
- [ ] Save and commit

### What I've Prepped
- `03_gemma_submission.ipynb` — Gemma 3n + LoRA for all 3 languages
- `03_colab_submission_guide.md` — step-by-step Colab instructions
- `docs/SCHEMATIC_PLAN.md` — detailed Altium schematic walkthrough
- Personal docs updated in D:\Fur Mich\

## Day 3 — Jul 7
- [ ] EDA: analyze language distribution, audio stats
- [ ] EDA notebook + visualizations
- [ ] First Zindi submission

## Day 4 — Jul 8
- [ ] Fine-tune Whisper-small on Lingala
- [ ] Model checkpoint

## Day 5 — Jul 9
- [ ] Fine-tune Whisper-small on Shona
- [ ] Model checkpoint

## Day 6 — Jul 10
- [ ] Fine-tune Whisper-small on Luganda
- [ ] Model checkpoint

## Day 7 — Jul 11
- [ ] Multilingual training — all 3 languages
- [ ] Combined model

## Day 8 — Jul 12
- [ ] Hyperparameter tuning (LR, batch, epochs)
- [ ] Optimized config

## Day 9 — Jul 13
- [ ] Data augmentation: speed perturbation, noise
- [ ] Augmented pipeline

## Day 10 — Jul 14
- [ ] Language-specific decoding strategies
- [ ] Improved WER/CER

## Day 11-29 — Jul 15 to Aug 2
- [ ] Iterative submissions (max 5/day)
- [ ] Phase 2 prep for unseen test data
- [ ] Final submissions and selection of top 2
- [ ] Challenge closes Aug 2

## Zindi Rules Quick Reference
- 5 submissions/day max, 200 total
- Open-source tools only (✅ Whisper, HuggingFace, PyTorch)
- No AutoML (✅ manual fine-tuning)
- External data allowed but must be disclosed
- Top 10 = code submission required within 48h
- **Must select 2 final submissions before challenge ends**
- Score = 0.5 × WER + 0.5 × CER
