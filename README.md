# CI/CD Pipeline Security Demo

This project demonstrates a secure CI/CD pipeline with GitHub Actions, including:
- ✅ Unit testing with Pytest
- 🔒 CodeQL analysis for vulnerabilities
- 🔍 Gitleaks scanning for secrets

## Setup

```bash
pip install -r requirements.txt
pytest
```

## GitHub Actions Workflow

A GitHub Actions workflow runs on push or pull request to the `main`, `demo-bad-practice` or `demo-bon-practice` branches.

Enjoy!
