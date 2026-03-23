from core.services.analysis_service import analyze_hvac_data


def test_advanced_diagnostics_generates_result():
    inputs = {
        "room_temp": 28.0,
        "setpoint_temp": 24.0,
        "outdoor_temp": 36.0,
        "chws": 7.0,
        "chwr": 14.0,
        "cws": 30.0,
        "cwr": 35.0,
        "chiller_power_kw": 120.0,
        "actual_cop": 2.8,
        "design_cop": 5.0,
        "tower_fan_speed": 65.0,
        "tower_approach": 6.0,
        "airflow_cfm": 8500.0,
        "water_ph": 9.1,
        "water_tds": 2100.0,
        "water_conductivity": 2500.0,
        "operating_hours": 10.0,
        "tariff": 0.12,
        "notes": "dirty filter",
    }

    result = analyze_hvac_data(inputs)
    assert "problems" in result
    assert "recommendations" in result
    assert result["confidence_score"] >= 0
