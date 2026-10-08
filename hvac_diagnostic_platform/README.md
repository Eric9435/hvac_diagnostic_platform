# HVAC Diagnostic Platform — Application

Streamlit HVAC calculations, rule-based diagnostics, local analysis history, comparisons, and reports.

## Run from this directory

Use Python 3 and a virtual environment.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
python -m pytest
```

Run from this directory inside an activated Python virtual environment. Review tariffs, design assumptions, and thresholds in `config.py`. Confidence scores are heuristic.

For full project features, architecture, configuration, and limitations, see the [repository README](../README.md).
