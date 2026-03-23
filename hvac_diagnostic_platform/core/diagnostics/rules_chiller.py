def evaluate_chiller_rules(inputs: dict) -> dict:
    problems = []
    causes = []
    recommendations = []
    severity = "info"

    actual_cop = inputs.get("actual_cop")
    design_cop = inputs.get("design_cop")
    chws = inputs.get("chws")
    chwr = inputs.get("chwr")
    power = inputs.get("chiller_power_kw")

    if actual_cop and design_cop and actual_cop < design_cop * 0.8:
        problems.append("Actual chiller COP is significantly below design COP.")
        causes.append("Chiller is consuming excess power for the delivered cooling effect.")
        recommendations.append("Check condenser condition, loading, refrigerant-side health, and control stability.")
        severity = "critical"

    if chws is not None and chwr is not None:
        delta_t = chwr - chws
        if delta_t < 4:
            problems.append("Chilled water delta-T is lower than expected.")
            causes.append("Possible low load, high flow, bypassing, or heat transfer inefficiency.")
            recommendations.append("Check chilled water flow, coil valves, bypass issues, and system balancing.")
            if severity == "info":
                severity = "warning"

    if power is not None and power > 0 and actual_cop and design_cop and actual_cop < design_cop:
        recommendations.append("Track kW, COP, and temperature trends over time to confirm persistent inefficiency.")

    return {
        "problems": problems,
        "causes": causes,
        "recommendations": recommendations,
        "severity": severity,
    }
