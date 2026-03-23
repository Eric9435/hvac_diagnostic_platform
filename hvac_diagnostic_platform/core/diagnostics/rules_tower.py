def evaluate_tower_rules(inputs: dict) -> dict:
    problems = []
    causes = []
    recommendations = []
    severity = "info"

    fan_speed = inputs.get("tower_fan_speed")
    approach = inputs.get("tower_approach")
    cws = inputs.get("cws")
    cwr = inputs.get("cwr")

    if fan_speed is not None and fan_speed < 80:
        problems.append("Cooling tower fan speed is below recommended level.")
        causes.append("Insufficient tower airflow may reduce condenser heat rejection.")
        recommendations.append("Check cooling tower motor speed, VFD output, fan blade condition, and belt tension.")
        severity = "critical"

    if approach is not None and approach > 5:
        problems.append("Cooling tower approach temperature is high.")
        causes.append("Cooling tower heat rejection performance may be degraded.")
        recommendations.append("Inspect tower fill, nozzle distribution, airflow path, and basin condition.")
        severity = "critical"

    if cws is not None and cwr is not None:
        if (cwr - cws) < 3:
            problems.append("Condenser water temperature range is low.")
            causes.append("Cooling tower or condenser heat rejection may be ineffective.")
            recommendations.append("Verify condenser water flow, tower fan operation, and water distribution.")
            if severity == "info":
                severity = "warning"

    return {
        "problems": problems,
        "causes": causes,
        "recommendations": recommendations,
        "severity": severity,
    }

