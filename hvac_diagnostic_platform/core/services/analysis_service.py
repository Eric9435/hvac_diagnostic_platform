from core.calculations.efficiency import calculate_efficiency_metrics
from core.calculations.energy_cost import calculate_total_system_power
from core.calculations.water_treatment import evaluate_water_treatment
from core.scoring.health_score import calculate_overall_health_score
from core.diagnostics.engine import run_diagnostics
from core.recommendations.action_engine import build_priority_actions


def analyze_hvac_data(inputs: dict) -> dict:
    water_result = evaluate_water_treatment(
        ph=inputs.get("water_ph"),
        tds=inputs.get("water_tds"),
        conductivity=inputs.get("water_conductivity"),
    )

    total_system_power_kw = calculate_total_system_power(
        chiller_power_kw=inputs.get("chiller_power_kw", 0.0),
        chw_pump_kw=inputs.get("chw_pump_kw", 0.0),
        cw_pump_kw=inputs.get("cw_pump_kw", 0.0),
        tower_fan_kw=inputs.get("tower_fan_kw", 0.0),
    )

    efficiency = calculate_efficiency_metrics(
        actual_power_kw=inputs.get("chiller_power_kw", 0.0),
        operating_hours=inputs.get("operating_hours", 0.0),
        tariff=inputs.get("tariff", 0.0),
        actual_cop=inputs.get("actual_cop"),
        design_cop=inputs.get("design_cop"),
    )

    diagnostics = run_diagnostics(inputs, water_result)

    comfort_status = "OK"
    if inputs.get("room_temp") and inputs.get("setpoint_temp"):
        if inputs["room_temp"] > inputs["setpoint_temp"] + 1:
            comfort_status = "Above Setpoint"
        elif inputs["room_temp"] < inputs["setpoint_temp"] - 1:
            comfort_status = "Below Setpoint"

    efficiency_status = "Good"
    if inputs.get("actual_cop") and inputs.get("design_cop"):
        if inputs["actual_cop"] < inputs["design_cop"]:
            efficiency_status = "Below Design"

    overall_score = calculate_overall_health_score(
        actual_cop=inputs.get("actual_cop"),
        design_cop=inputs.get("design_cop"),
        tower_fan_speed=inputs.get("tower_fan_speed"),
        water_health_score=water_result["water_health_score"],
        room_temp=inputs.get("room_temp", 0.0),
        setpoint_temp=inputs.get("setpoint_temp", 0.0),
    )

    priority_actions = build_priority_actions(diagnostics["recommendations"])

    return {
        "total_system_power_kw": total_system_power_kw,
        "ideal_power_kw": efficiency["ideal_power_kw"],
        "wasted_power_kw": efficiency["wasted_power_kw"],
        "wasted_energy_kwh": efficiency["wasted_energy_kwh"],
        "wasted_cost": efficiency["wasted_cost"],
        "monthly_loss": efficiency["monthly_loss"],
        "annual_loss": efficiency["annual_loss"],
        "efficiency_loss_percent": efficiency["efficiency_loss_percent"],
        "comfort_status": comfort_status,
        "efficiency_status": efficiency_status,
        "overall_score": overall_score,
        "confidence_score": diagnostics["confidence_score"],
        "water_status": water_result["water_status"],
        "water_health_score": water_result["water_health_score"],
        "problems": diagnostics["problems"],
        "causes": diagnostics["causes"],
        "recommendations": priority_actions,
        "severity": diagnostics["severity"],
    }
