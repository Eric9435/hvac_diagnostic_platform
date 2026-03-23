# Step 38 — `tests/test_efficiency.py`

```python
from core.calculations.efficiency import calculate_efficiency_metrics


def test_efficiency_metrics():
    result = calculate_efficiency_metrics(
        actual_power_kw=120,
        operating_hours=10,
        tariff=0.12,
        actual_cop=2.8,
        design_cop=5.0,
    )
    assert result["wasted_energy_kwh"] >= 0
    assert result["wasted_cost"] >= 0
