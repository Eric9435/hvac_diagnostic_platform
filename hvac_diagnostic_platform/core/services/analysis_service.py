from core.calculations.efficiency import calculate_efficiency_metrics
from core.calculations.energy_cost import calculate_total_system_power
from core.calculations.water_treatment import evaluate_water_treatment
from core.scoring.health_score import calculate_overall_health_score
from core.scoring.confidence_score import calculate_confidence_score

from core.diagnostics.rules_tower import evaluate_tower_rules
from core.diagnostics.rules_water import evaluate_water_rules
from core.diagnostics.rules_ahu import evaluate_ahu_rules
from core.diagnostics.rules_chiller import evaluate_chiller_rules
from core.diagnostics.root_cause import infer_root_causes

from core.recommendations.action_engine import build_priority_actions


def _max_severity(severities: list[str]) -> str:
    if "critical" in severities:
        return "critical"
    if "warning" in severities:
        return "warning"
    return "info"


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

    tower_diag = evaluate_tower_rules(inputs)
    water_diag = evaluate_water_rules(inputs)
    ahu_diag = evaluate_ahu_rules(inputs)
    chiller_diag = evaluate_chiller_rules(inputs)

    all_problems = (
        tower_diag["problems"]
        + water_diag["problems"]
        + ahu_diag["problems"]
        + chiller_diag["problems"]
    )
    all_causes = (
        tower_diag["causes"]
        + water_diag["causes"]
        + ahu_diag["causes"]
        + chiller_diag["causes"]
    )
    all_recommendations = (
        tower_diag["recommendations"]
        + water_diag["recommendations"]
        + ahu_diag["recommendations"]
        + chiller_diag["recommendations"]
    )

    root_causes = infer_root_causes(all_causes)
    priority_actions = build_priority_actions(all_recommendations)

    comfort_status = "OK"
    if inputs.get("room_temp") is not None and inputs.get("setpoint_temp") is not None:
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

    confidence_score = calculate_confidence_score(inputs, len(all_problems))

    severity = _max_severity(
        [
            tower_diag["severity"],
            water_diag["severity"],
            ahu_diag["severity"],
            chiller_diag["severity"],
        ]
    )

    # subsystem scores
    chiller_score = 100.0
    if inputs.get("actual_cop") and inputs.get("design_cop") and inputs["design_cop"] > 0:
        ratio = inputs["actual_cop"] / inputs["design_cop"]
        chiller_score = max(min(round(ratio * 100, 2), 100.0), 0.0)

    tower_score = 100.0
    if inputs.get("tower_fan_speed") is not None and inputs.get("tower_approach") is not None:
        tower_score -= max(0, 80 - inputs["tower_fan_speed"]) * 0.5
        tower_score -= max(0, inputs["tower_approach"] - 5) * 8
        tower_score = max(round(tower_score, 2), 0.0)

    ahu_score = 100.0
    if inputs.get("airflow_cfm") is not None and inputs["airflow_cfm"] < 8000:
        ahu_score -= 20
    if "dirty" in (inputs.get("notes") or "").lower():
        ahu_score -= 10
    ahu_score = max(round(ahu_score, 2), 0.0)

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
        "confidence_score": confidence_score,
        "water_status": water_result["water_status"],
        "water_health_score": water_result["water_health_score"],
        "problems": all_problems,
        "causes": all_causes,
        "root_causes": root_causes,
        "recommendations": priority_actions,
        "severity": severity,
        "chiller_score": chiller_score,
        "tower_score": tower_score,
        "ahu_score": ahu_score,
    }
from core.calculations.efficiency import calculate_efficiency_metrics
from core.calculations.energy_cost import calculate_total_system_power
from core.calculations.water_treatment import evaluate_water_treatment
from core.scoring.health_score import calculate_overall_health_score
from core.scoring.confidence_score import calculate_confidence_score

from core.diagnostics.rules_tower import evaluate_tower_rules
from core.diagnostics.rules_water import evaluate_water_rules
from core.diagnostics.rules_ahu import evaluate_ahu_rules
from core.diagnostics.rules_chiller import evaluate_chiller_rules
from core.diagnostics.root_cause import infer_root_causes

from core.recommendations.action_engine import build_priority_actions


def _max_severity(severities: list[str]) -> str:
    if "critical" in severities:
        return "critical"
    if "warning" in severities:
        return "warning"
    return "info"


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

    tower_diag = evaluate_tower_rules(inputs)
    water_diag = evaluate_water_rules(inputs)
    ahu_diag = evaluate_ahu_rules(inputs)
    chiller_diag = evaluate_chiller_rules(inputs)

    all_problems = (
        tower_diag["problems"]
        + water_diag["problems"]
        + ahu_diag["problems"]
        + chiller_diag["problems"]
    )
    all_causes = (
        tower_diag["causes"]
        + water_diag["causes"]
        + ahu_diag["causes"]
        + chiller_diag["causes"]
    )
    all_recommendations = (
        tower_diag["recommendations"]
        + water_diag["recommendations"]
        + ahu_diag["recommendations"]
        + chiller_diag["recommendations"]
    )

    root_causes = infer_root_causes(all_causes)
    priority_actions = build_priority_actions(all_recommendations)

    comfort_status = "OK"
    if inputs.get("room_temp") is not None and inputs.get("setpoint_temp") is not None:
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

    confidence_score = calculate_confidence_score(inputs, len(all_problems))

    severity = _max_severity(
        [
            tower_diag["severity"],
            water_diag["severity"],
            ahu_diag["severity"],
            chiller_diag["severity"],
        ]
    )

    # subsystem scores
    chiller_score = 100.0
    if inputs.get("actual_cop") and inputs.get("design_cop") and inputs["design_cop"] > 0:
        ratio = inputs["actual_cop"] / inputs["design_cop"]
        chiller_score = max(min(round(ratio * 100, 2), 100.0), 0.0)

    tower_score = 100.0
    if inputs.get("tower_fan_speed") is not None and inputs.get("tower_approach") is not None:
        tower_score -= max(0, 80 - inputs["tower_fan_speed"]) * 0.5
        tower_score -= max(0, inputs["tower_approach"] - 5) * 8
        tower_score = max(round(tower_score, 2), 0.0)

    ahu_score = 100.0
    if inputs.get("airflow_cfm") is not None and inputs["airflow_cfm"] < 8000:
        ahu_score -= 20
    if "dirty" in (inputs.get("notes") or "").lower():
        ahu_score -= 10
    ahu_score = max(round(ahu_score, 2), 0.0)

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
        "confidence_score": confidence_score,
        "water_status": water_result["water_status"],
        "water_health_score": water_result["water_health_score"],
        "problems": all_problems,
        "causes": all_causes,
        "root_causes": root_causes,
        "recommendations": priority_actions,
        "severity": severity,
        "chiller_score": chiller_score,
        "tower_score": tower_score,
        "ahu_score": ahu_score,
    }

