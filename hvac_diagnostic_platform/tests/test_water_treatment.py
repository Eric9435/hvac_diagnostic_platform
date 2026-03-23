from core.calculations.water_treatment import evaluate_water_treatment


def test_water_treatment_status():
    result = evaluate_water_treatment(ph=9.1, tds=2100, conductivity=2500)
    assert result["water_status"] in ["Good", "Warning", "Poor"]
    assert result["water_health_score"] >= 0
