from core.services.export_service import td


def build_executive_summary(record: dict, lang: str = "en") -> str:
    lines = [
        td("executive_summary", lang),
        "=" * 40,
        f"{td('site_name', lang):<22}: {record.get('site_name', '-')}",
        f"{td('building_name', lang):<22}: {record.get('building_name', '-')}",
        f"{td('equipment_name', lang):<22}: {record.get('equipment_name', '-')}",
        f"{td('equipment_tag', lang):<22}: {record.get('equipment_tag', '-')}",
        f"{td('ac_type', lang):<22}: {record.get('ac_type', '-')}",
        f"{td('analysis_mode', lang):<22}: {record.get('analysis_mode', '-')}",
        f"{td('operator_name', lang):<22}: {record.get('operator_name', '-')}",
        f"{td('date', lang):<22}: {record.get('analysis_date', '-')}",
        f"{td('time', lang):<22}: {record.get('analysis_time', '-')}",
        "",
        td("kpis", lang),
        "-" * 40,
        f"{td('room_temp', lang):<22}: {record.get('room_temp', '-')}",
        f"{td('setpoint_temp', lang):<22}: {record.get('setpoint_temp', '-')}",
        f"{td('outdoor_temp', lang):<22}: {record.get('outdoor_temp', '-')}",
        f"{td('actual_cop', lang):<22}: {record.get('actual_cop', '-')}",
        f"{td('design_cop', lang):<22}: {record.get('design_cop', '-')}",
        f"{td('total_system_power', lang):<22}: {record.get('total_system_power_kw', '-')}",
        f"{td('wasted_energy', lang):<22}: {record.get('wasted_energy_kwh', '-')}",
        f"{td('wasted_cost', lang):<22}: {record.get('wasted_cost', '-')}",
        f"{td('monthly_loss', lang):<22}: {record.get('monthly_loss', '-')}",
        f"{td('annual_loss', lang):<22}: {record.get('annual_loss', '-')}",
        f"{td('comfort_status', lang):<22}: {record.get('comfort_status', '-')}",
        f"{td('efficiency_status', lang):<22}: {record.get('efficiency_status', '-')}",
        f"{td('overall_score', lang):<22}: {record.get('overall_score', '-')}",
        f"{td('confidence_score', lang):<22}: {record.get('confidence_score', '-')}",
        "",
        td("detected_problems", lang),
        "-" * 40,
    ]

    problems = record.get("detected_problems", [])
    if problems:
        lines.extend([f"- {item}" for item in problems])
    else:
        lines.append("- None")

    lines.extend(["", td("likely_causes", lang), "-" * 40])
    causes = record.get("likely_causes", [])
    if causes:
        lines.extend([f"- {item}" for item in causes])
    else:
        lines.append("- None")

    lines.extend(["", td("recommendations", lang), "-" * 40])
    recommendations = record.get("recommendations", [])
    if recommendations:
        lines.extend([f"- {item}" for item in recommendations])
    else:
        lines.append("- None")

    notes = record.get("notes")
    if notes:
        lines.extend(["", td("notes", lang), "-" * 40, notes])

    return "\n".join(lines)

