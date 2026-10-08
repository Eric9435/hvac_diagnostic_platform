# HVAC Diagnostic Platform

A Streamlit engineering application for reviewing HVAC efficiency, identifying rule-based faults, estimating energy/cost impact, and recording analyses.

## Features

- Basic and advanced analysis workflows.
- AHU, chiller, cooling-tower, and water-treatment diagnostic rules.
- Efficiency calculations, health/confidence scores, and prioritized recommendations.
- Energy-loss and cost estimates.
- Results dashboard, analysis history, comparisons, and reports.
- Local SQLite persistence with timestamps.
- English, Myanmar, and dual-language interface options.

## Technology

Python, Streamlit, Pandas, Plotly, Pydantic, SQLite, and Pytest.

## Local development

Use Python 3 and an isolated virtual environment. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r hvac_diagnostic_platform/requirements.txt
cd hvac_diagnostic_platform
python -m streamlit run app.py
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. Open the local URL printed by Streamlit, usually http://localhost:8501.

## Verification

From the inner application directory:

```bash
python -m pytest
```

Tests cover efficiency, diagnostics, reporting, and water-treatment calculations. The command is provided for reproduction; this README update does not claim a fresh test run.

## Architecture

| Directory | Responsibility |
| --- | --- |
| `core/calculations/` | Efficiency, energy cost, and water calculations |
| `core/diagnostics/` | Equipment rules and root-cause aggregation |
| `core/scoring/` | Health and confidence heuristics |
| `core/services/` | Analysis orchestration and exports |
| `ui/` | Pages, charts, and forms |
| `storage/` and `database/` | SQLite records and schema |
| `tests/` | Automated checks |

## Configuration and limits

Review tariffs, design COP, currency, and fault thresholds in `config.py`. The default economic assumptions are project-specific. Diagnostic confidence scores are heuristics, not probabilities from a validated trained model. This is an analysis prototype; physical equipment integration and field validation are separate work.

## Maintainer

[Aung Phone Myat (Eric)](https://github.com/Eric9435)
