def evaluate_ahu_rules(inputs: dict) -> dict:
    problems = []
    causes = []
    recommendations = []
    severity = "info"

    room_temp = inputs.get("room_temp")
    setpoint = inputs.get("setpoint_temp")
    airflow = inputs.get("airflow_cfm")
    notes = (inputs.get("notes") or "").lower()

    if room_temp is not None and setpoint is not None and room_temp > setpoint + 1:
        if airflow is not None and airflow < 8000:
            problems.append("Room temperature is above setpoint and airflow is low.")
            causes.append("AHU air delivery may be insufficient.")
            recommendations.append("Check filter condition, fan speed, damper position, and duct restriction.")
            severity = "warning"

    if "filter" in notes and "dirty" in notes:
        problems.append("Dirty AHU filter observed.")
        causes.append("Dirty filter may reduce airflow and cooling delivery.")
        recommendations.append("Clean or replace AHU filter and recheck airflow.")
        severity = "warning"

    if "coil" in notes and "dirty" in notes:
        problems.append("Dirty cooling coil observed.")
        causes.append("Coil fouling may reduce heat transfer performance.")
        recommendations.append("Clean AHU/FCU cooling coil and inspect condensate drainage.")
        severity = "warning"

    return {
        "problems": problems,
        "causes": causes,
        "recommendations": recommendations,
        "severity": severity,
    }

