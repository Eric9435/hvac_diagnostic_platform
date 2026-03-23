def calculate_confidence_score(inputs: dict, total_problems: int) -> float:
    important_fields = [
        "room_temp",
        "setpoint_temp",
        "outdoor_temp",
        "chws",
        "chwr",
        "cws",
        "cwr",
        "chiller_power_kw",
        "actual_cop",
        "design_cop",
        "tower_fan_speed",
        "tower_approach",
        "airflow_cfm",
        "water_ph",
        "water_tds",
        "water_conductivity",
    ]

    available = sum(1 for field in important_fields if inputs.get(field) is not None)
    completeness_ratio = available / len(important_fields)

    base_score = completeness_ratio * 70

    if total_problems >= 4:
        base_score += 20
    elif total_problems >= 2:
        base_score += 10
    elif total_problems >= 1:
        base_score += 5

    return round(min(base_score, 100.0), 2)
