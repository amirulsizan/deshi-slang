# deshi-slang

Open-source Bengali slang and harmful language dataset for AI moderation, content filtering, and social media safety systems.

This repository provides:
- A lightweight dataset schema and sample data in JSONL format.
- Contribution guidelines and an annotation taxonomy for consistent labeling.
- A small validation script and GitHub Actions workflow to run basic checks.

Goals:
- Make Bengali (Bangla) harmful-language research accessible and reproducible.
- Provide clear annotation guidance so contributors can expand the dataset.
- License the dataset for research and responsible use.

See the dataset card: [DATASET_CARD.md](DATASET_CARD.md)

Quick start

Install requirements and run the dataset validator on the sample file:

```bash
python -m pip install -r requirements.txt
python scripts/validate_dataset.py data/sample.jsonl
```

If you'd like, I can initialize a git repo and make an initial commit here.
