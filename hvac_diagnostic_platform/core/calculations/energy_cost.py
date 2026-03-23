def calculate_total_system_power(chiller_power_kw: float, chw_pump_kw: float = 0.0, cw_pump_kw: float = 0.0, tower_fan_kw: float = 0.0) -> float:
    return round((chiller_power_kw or 0.0) + (chw_pump_kw or 0.0) + (cw_pump_kw or 0.0) + (tower_fan_kw or 0.0), 2)
