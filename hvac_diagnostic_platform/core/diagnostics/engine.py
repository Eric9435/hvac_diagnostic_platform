from config import THRESHOLDS


def run_diagnostics(inputs: dict, water_result: dict) -> dict:
    problems = []
    causes = []
    recommendations = []
    severity = "info"

    room_temp = inputs.get("room_temp")
    setpoint_temp = inputs.get("setpoint_temp")
    actual_cop = inputs.get("actual_cop")
    design_cop = inputs.get("design_cop")
    tower_fan_speed = inputs.get("tower_fan_speed")
    tower_approach = inputs.get("tower_approach")
    airflow_cfm = inputs.get("airflow_cfm")
    notes = inputs.get("notes", "")

    if room_temp is not None and setpoint_temp is not None:
        if room_temp > setpoint_temp + THRESHOLDS["room_temp_high_offset"]:
            problems.append("Room temperature is above setpoint.")
            causes.append("Cooling delivery may be insufficient.")
            recommendations.append("Check chilled water temperature, airflow, and load condition.")
            severity = "warning"

    if actual_cop and design_cop and design_cop > 0:
        if actual_cop < design_cop * THRESHOLDS["cop_low_ratio"]:
            problems.append("Actual COP is significantly below design COP.")
            causes.append("System efficiency is reduced.")
            recommendations.append("Inspect chiller loading, condenser condition, and cooling tower performance.")
            severity = "critical"

    if tower_fan_speed is not None and tower_fan_speed < THRESHOLDS["tower_fan_speed_low"]:
        problems.append("Cooling tower fan speed is below normal range.")
        causes.append("Tower airflow may be insufficient, reducing heat rejection.")
        recommendations.append("Check motor speed, VFD output, fan blades, belt tension, and bearings.")
        severity = "critical"

    if tower_approach is not None and tower_approach > THRESHOLDS["tower_approach_high"]:
        problems.append("Cooling tower approach temperature is high.")
        causes.append("Cooling tower performance may be degraded.")
        recommendations.append("Inspect tower fill, nozzle, airflow path, and condenser water temperature trend.")
        severity = "critical"

    if water_result["water_status"] != "Good":
        problems.append("Water treatment condition is outside recommended range.")
        causes.append("Poor water quality may be causing fouling or scale buildup.")
        recommendations.append("Review pH, TDS, conductivity, chemical dosing, blowdown, and cleaning schedule.")
        severity = "critical"

    if airflow_cfm is not None and airflow_cfm < 8000:
        problems.append("AHU airflow appears low.")
        causes.append("Air delivery may be restricted.")
        recommendations.append("Check filter condition, fan speed, damper position, and coil cleanliness.")
        severity = "warning"

    if "dirty" in notes.lower():
        causes.append("Observed dirty condition may be contributing to lower performance.")
        recommendations.append("Inspect and clean affected components.")

    confidence = 60.0
    if len(problems) >= 3:
        confidence = 85.0
    elif len(problems) == 2:
        confidence = 75.0
    elif len(problems) == 1:
        confidence = 65.0

    return {
        "severity": severity,
        "problems": problems,
        "causes": causes,
        "recommendations": recommendations,
        "confidence_score": confidence,
    }
