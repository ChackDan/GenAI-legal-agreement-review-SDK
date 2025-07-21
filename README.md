# Legal Agreement Analyzer SDK (Python)

This is a Python client SDK for interacting with the Legal Agreement Analyzer API.

## Installation

```bash
pip install requests
```

## Usage

```python
from legal_sdk.client import LegalAnalyzerClient

client = LegalAnalyzerClient(base_url="https://api.oci-legal-analyzer.example.com/v1")

# Example: Parse agreement
response = client.parse_agreement(agreement_id="AG12345", file_path="sample.pdf", file_type="pdf")
print(response)
```

## Features

- Agreement Parsing
- Clause Mapping
- Clause Similarity Search
- LLM-based Clause Analysis
- Feedback Submission
- Model Training Trigger
