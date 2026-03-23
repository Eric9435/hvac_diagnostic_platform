from config import THRESHOLDS


def evaluate_water_treatment(ph: float | None, tds: float | None, conductivity: float | None) -> dict:
    issues = []
    risk_score = 100.0

    if ph is not None:
        if ph < THRESHOLDS["water_ph_low"] or ph > THRESHOLDS["water_ph_high"]:
            issues.append("Water pH is outside recommended range.")
            risk_score -= 25

    if tds is not None and tds > THRESHOLDS["water_tds_high"]:
        issues.append("TDS is high, increasing fouling/scaling risk.")
        risk_score -= 35

    if conductivity is not None and conductivity > 2000:
        issues.append("Conductivity is high, indicating potential water quality concern.")
        risk_score -= 20

    status = "Good"
    if risk_score < 80:
        status = "Warning"
    if risk_score < 60:
        status = "Poor"

    return {
        "water_status": status,
        "water_health_score": max(round(risk_score, 2), 0.0),
        "water_issues": issues,
    }
