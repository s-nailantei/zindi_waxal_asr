# Day 2: First Zindi Submission — Step by Step

## Goal
Run the baseline, generate predictions, upload to Zindi leaderboard.

## Instructions

### Step 1: Upload notebooks to Colab
1. Go to https://colab.research.google.com
2. File → Upload notebook → select `01_waxal_baseline_whisper.ipynb`
3. Also upload `03_gemma_submission.ipynb` (preferred — matches official starter)

### Step 2: Set runtime
1. Runtime → Change runtime type → T4 GPU
2. (Free tier works, Pro recommended)

### Step 3: Run
1. Run all cells (Runtime → Run all)
2. Training should take ~30-60 min on subset, 2-4 hrs on full
3. If Colab disconnects, use the checkpoint save/restore cells

### Step 4: Download submission
1. After the final cell, download `submissions/baseline_whisper_submission.csv`
2. Or the Gemma notebook generates it directly

### Step 5: Submit to Zindi
1. Go to https://zindi.africa/competitions/google-waxal-asr-challenge
2. Click "Submit" button
3. Upload the CSV file
4. Wait for processing (few minutes)
5. Check your score on the public leaderboard

### Step 6: Report back
Run `git add -A && git commit -m "Day 2: first submission"`
Push to GitHub.

Tell me:
- Public leaderboard score (WER + CER)
- Any errors during run
- How long training took
