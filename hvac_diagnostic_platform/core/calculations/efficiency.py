def calculate_efficiency_metrics(
    actual_power_kw: float,
    operating_hours: float,
    tariff: float,
    actual_cop: float | None,
    design_cop: float | None,
) -> dict:
    actual_power_kw = actual_power_kw or 0.0
    operating_hours = operating_hours or 0.0
    tariff = tariff or 0.0

    if actual_cop and design_cop and actual_cop > 0 and design_cop > 0:
        ideal_power_kw = actual_power_kw * (actual_cop / design_cop)
    else:
        ideal_power_kw = actual_power_kw

    wasted_power_kw = max(actual_power_kw - ideal_power_kw, 0.0)
    wasted_energy_kwh = wasted_power_kw * operating_hours
    wasted_cost = wasted_energy_kwh * tariff
    monthly_loss = wasted_cost * 30
    annual_loss = wasted_cost * 365

    if actual_cop and design_cop and actual_cop < design_cop:
        efficiency_loss_percent = ((design_cop - actual_cop) / design_cop) * 100
    else:
        efficiency_loss_percent = 0.0

    return {
        "ideal_power_kw": round(ideal_power_kw, 2),
        "wasted_power_kw": round(wasted_power_kw, 2),
        "wasted_energy_kwh": round(wasted_energy_kwh, 2),
        "wasted_cost": round(wasted_cost, 2),
        "monthly_loss": round(monthly_loss, 2),
        "annual_loss": round(annual_loss, 2),
        "efficiency_loss_percent": round(efficiency_loss_percent, 2),
    }
