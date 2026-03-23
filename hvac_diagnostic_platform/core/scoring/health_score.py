def calculate_overall_health_score(
    actual_cop: float | None,
    design_cop: float | None,
    tower_fan_speed: float | None,
    water_health_score: float,
    room_temp: float,
    setpoint_temp: float,
) -> float:
    score = 100.0

    if actual_cop and design_cop and design_cop > 0:
        ratio = actual_cop / design_cop
        if ratio < 1:
            score -= (1 - ratio) * 40

    if tower_fan_speed is not None and tower_fan_speed < 80:
        score -= 15

    score -= (100 - water_health_score) * 0.2

    if room_temp > setpoint_temp + 1:
        score -= 15

    return max(round(score, 2), 0.0)
