# Contributing

Thank you for contributing to `deshi-slang`.

How to contribute

1. Fork the repository and create a branch for your work.
2. Add new examples to `data/` in JSONL format following the schema in `data/schema.yml`.
3. Run the validator: `python scripts/validate_dataset.py data/your_file.jsonl`.
4. Open a pull request. Describe data provenance and annotation process.

Annotation guidelines (summary):
- Use the taxonomy in `DATASET_CARD.md` (15 labels total: 6 original + 9 extended moderation labels).
- Prefer conservative labeling: if unsure between multiple labels, add both/all applicable labels and add an explanation in `source` or PR description.
- Severity scoring: assign `severity_score` 1–5 based on content severity (1=mild, 5=extreme).
- Obfuscation detection: set `is_obfuscated: true` for intentionally misspelled, spaced, or character-substituted variants.
- Do not add personally identifiable information (PII) or private data.
- Avoid collecting content that promotes violence or glorifies hate — contact maintainers for edge cases.

Ethics & privacy
- Contributors must ensure they have rights to redistribute any collected content.
- Remove or redact PII before contribution.
- For large crawled datasets, include a provenance file describing collection, filters, and consent where applicable.

Code of conduct
Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).
