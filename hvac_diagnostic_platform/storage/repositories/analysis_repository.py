import json
from storage.db import get_connection


def save_analysis_record(payload: dict) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analyses (
            site_name, building_name, equipment_name, equipment_tag, ac_type, analysis_mode,
            operator_name, analysis_date, analysis_time, analysis_month, analysis_year, timestamp,
            room_temp, setpoint_temp, outdoor_temp,
            chws, chwr, cws, cwr,
            chiller_power_kw, operating_hours, tariff,
            actual_cop, design_cop, chw_flow, cw_flow, airflow_cfm,
            tower_fan_speed, tower_approach,
            water_ph, water_tds, water_conductivity,
            total_system_power_kw, ideal_power_kw, wasted_power_kw, wasted_energy_kwh,
            wasted_cost, monthly_loss, annual_loss,
            comfort_status, efficiency_status, overall_score, confidence_score,
            detected_problems, likely_causes, recommendations, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            payload.get("site_name"),
            payload.get("building_name"),
            payload.get("equipment_name"),
            payload.get("equipment_tag"),
            payload.get("ac_type"),
            payload.get("analysis_mode"),
            payload.get("operator_name"),
            payload.get("analysis_date"),
            payload.get("analysis_time"),
            payload.get("analysis_month"),
            payload.get("analysis_year"),
            payload.get("timestamp"),
            payload.get("room_temp"),
            payload.get("setpoint_temp"),
            payload.get("outdoor_temp"),
            payload.get("chws"),
            payload.get("chwr"),
            payload.get("cws"),
            payload.get("cwr"),
            payload.get("chiller_power_kw"),
            payload.get("operating_hours"),
            payload.get("tariff"),
            payload.get("actual_cop"),
            payload.get("design_cop"),
            payload.get("chw_flow"),
            payload.get("cw_flow"),
            payload.get("airflow_cfm"),
            payload.get("tower_fan_speed"),
            payload.get("tower_approach"),
            payload.get("water_ph"),
            payload.get("water_tds"),
            payload.get("water_conductivity"),
            payload.get("total_system_power_kw"),
            payload.get("ideal_power_kw"),
            payload.get("wasted_power_kw"),
            payload.get("wasted_energy_kwh"),
            payload.get("wasted_cost"),
            payload.get("monthly_loss"),
            payload.get("annual_loss"),
            payload.get("comfort_status"),
            payload.get("efficiency_status"),
            payload.get("overall_score"),
            payload.get("confidence_score"),
            json.dumps(payload.get("problems", [])),
            json.dumps(payload.get("causes", [])),
            json.dumps(payload.get("recommendations", [])),
            payload.get("notes"),
        ),
    )

    conn.commit()
    analysis_id = cursor.lastrowid
    conn.close()
    return analysis_id


def fetch_all_analyses() -> list[dict]:
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT id, site_name, equipment_name, ac_type, analysis_mode,
               analysis_date, analysis_time, operator_name,
               wasted_energy_kwh, wasted_cost, overall_score, confidence_score
        FROM analyses
        ORDER BY id DESC
        """
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
