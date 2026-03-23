def evaluate_water_rules(inputs: dict) -> dict:
    problems = []
    causes = []
    recommendations = []
    severity = "info"

    ph = inputs.get("water_ph")
    tds = inputs.get("water_tds")
    conductivity = inputs.get("water_conductivity")

    if ph is not None and (ph < 6.5 or ph > 8.5):
        problems.append("Water pH is outside acceptable range.")
        causes.append("Improper pH can accelerate corrosion or scaling.")
        recommendations.append("Review chemical dosing and retest water chemistry.")
        severity = "warning"

    if tds is not None and tds > 1500:
        problems.append("Water TDS is high.")
        causes.append("High dissolved solids may increase fouling and scaling risk.")
        recommendations.append("Check blowdown control and review water treatment settings.")
        severity = "critical"

    if conductivity is not None and conductivity > 2000:
        problems.append("Water conductivity is high.")
        causes.append("Poor water quality may reduce heat transfer efficiency.")
        recommendations.append("Inspect condenser/evaporator fouling condition and review treatment records.")
        severity = "critical"

    return {
        "problems": problems,
        "causes": causes,
        "recommendations": recommendations,
        "severity": severity,
    }

