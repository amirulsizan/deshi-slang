# Dataset Card — deshi-slang

Dataset name: deshi-slang

Short description:
Open dataset of Bengali slang, abusive, and potentially harmful language intended for research in moderation and content filtering. Includes labels and metadata to support model training and evaluation.

Languages: Bengali (bn)

Dataset structure:
- Format: JSON Lines (`.jsonl`), one JSON object per line.
- Fields:
  - `id` (string): unique identifier
  - `text` (string): raw text in Bengali (UTF-8)
  - `labels` (array[string]): one or more labels from the taxonomy
  - `language` (string): ISO code (e.g. `bn`)
  - `source` (string, optional): origin or source metadata
  - `annotator_id` (string, optional)
  - `split` (string): `train`, `validation`, or `test`

Label taxonomy (initial):
- `abusive`: general insults and abusive expressions
- `slur`: identity-targeted derogatory terms
- `derogatory`: non-identity-based denigration
- `sexual`: sexual content or explicit language
- `slang`: colloquial/slang that may be offensive in context
- `neutral`: non-harmful content

Licensing:
- Code and tooling: MIT License (see `LICENSE`).
- Dataset content: CC BY 4.0 (see `LICENSE-DATA`).

Collection and annotation notes:
- This repository starts with a small synthetic/sample set for tooling and schema.
- Before adding large-scale real examples, follow the `CONTRIBUTING.md` annotation workflow and ethical guidelines.
