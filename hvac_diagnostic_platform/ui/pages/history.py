import streamlit as st
import pandas as pd

from storage.repositories.analysis_repository import fetch_all_analyses, fetch_analysis_by_id
from core.services.export_service import td
from ui.components.header import render_hero


def render_history_input_panel(record: dict) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Saved Input Data / သိမ်းထားသော Input Data")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### General")
        st.write(f"**Site Name:** {record.get('site_name', '-')}")
        st.write(f"**Building Name:** {record.get('building_name', '-')}")
        st.write(f"**Equipment Name:** {record.get('equipment_name', '-')}")
        st.write(f"**Equipment Tag:** {record.get('equipment_tag', '-')}")
        st.write(f"**AC Type:** {record.get('ac_type', '-')}")
        st.write(f"**Analysis Mode:** {record.get('analysis_mode', '-')}")
        st.write(f"**Operator Name:** {record.get('operator_name', '-')}")
        st.write(f"**Date:** {record.get('analysis_date', '-')}")
        st.write(f"**Time:** {record.get('analysis_time', '-')}")

    with col2:
        st.markdown("### Room / Water Side")
        st.write(f"**Room Temp (°C):** {record.get('room_temp', '-')}")
        st.write(f"**Setpoint Temp (°C):** {record.get('setpoint_temp', '-')}")
        st.write(f"**Outdoor Temp (°C):** {record.get('outdoor_temp', '-')}")
        st.write(f"**CHWS (°C):** {record.get('chws', '-')}")
        st.write(f"**CHWR (°C):** {record.get('chwr', '-')}")
        st.write(f"**CHW Flow (kg/s):** {record.get('chw_flow', '-')}")
        st.write(f"**CWS Entering (°C):** {record.get('cws', '-')}")
        st.write(f"**CWS Leaving (°C):** {record.get('cwr', '-')}")
        st.write(f"**CW Flow (kg/s):** {record.get('cw_flow', '-')}")

    with col3:
        st.markdown("### Equipment / Cost")
        st.write(f"**Chiller Power (kW):** {record.get('chiller_power_kw', '-')}")
        st.write(f"**Actual COP:** {record.get('actual_cop', '-')}")
        st.write(f"**Design COP:** {record.get('design_cop', '-')}")
        st.write(f"**AHU Airflow (CFM):** {record.get('airflow_cfm', '-')}")
        st.write(f"**Tower Fan Speed (%):** {record.get('tower_fan_speed', '-')}")
        st.write(f"**Tower Approach (°C):** {record.get('tower_approach', '-')}")
        st.write(f"**Water pH:** {record.get('water_ph', '-')}")
        st.write(f"**Water TDS:** {record.get('water_tds', '-')}")
        st.write(f"**Water Conductivity:** {record.get('water_conductivity', '-')}")
        st.write(f"**Operating Hours:** {record.get('operating_hours', '-')}")
        st.write(f"**Tariff:** {record.get('tariff', '-')}")

    st.markdown("</div>", unsafe_allow_html=True)


def render_history_output_panel(record: dict) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Saved Output Summary / သိမ်းထားသော Output Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Performance")
        st.write(f"**Total System Power (kW):** {record.get('total_system_power_kw', '-')}")
        st.write(f"**Ideal Power (kW):** {record.get('ideal_power_kw', '-')}")
        st.write(f"**Wasted Power (kW):** {record.get('wasted_power_kw', '-')}")
        st.write(f"**Wasted Energy (kWh):** {record.get('wasted_energy_kwh', '-')}")

    with col2:
        st.markdown("### Cost / Loss")
        st.write(f"**Wasted Cost:** {record.get('wasted_cost', '-')}")
        st.write(f"**Monthly Loss:** {record.get('monthly_loss', '-')}")
        st.write(f"**Annual Loss:** {record.get('annual_loss', '-')}")
        st.write(f"**Comfort Status:** {record.get('comfort_status', '-')}")

    with col3:
        st.markdown("### Score / Confidence")
        st.write(f"**Efficiency Status:** {record.get('efficiency_status', '-')}")
        st.write(f"**Overall Score:** {record.get('overall_score', '-')}")
        st.write(f"**Confidence Score:** {record.get('confidence_score', '-')}")

    st.markdown("</div>", unsafe_allow_html=True)


def render_history_page() -> None:
    lang = st.session_state.get("lang", "dual")

    render_hero(
        td("history", lang),
        "Review saved HVAC analyses, inspect input-output records, and revisit engineering diagnostics over time.",
    )

    rows = fetch_all_analyses()
    if not rows:
        st.markdown(
            """
            <div class="empty-box">
                <h4>No Saved Records</h4>
                <p>Run a new analysis first to create history records.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    df = pd.DataFrame(rows)

    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Saved Records Table / သိမ်းထားသော မှတ်တမ်းများ")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader(td("view_record_details", lang))

    options = {
        f"ID {row['id']} | {row['site_name']} | {row['equipment_name']} | {row['analysis_date']} {row['analysis_time']}": row["id"]
        for row in rows
    }

    selected_label = st.selectbox(td("select_analysis_record", lang), list(options.keys()))
    selected_id = options[selected_label]
    st.markdown("</div>", unsafe_allow_html=True)

    record = fetch_analysis_by_id(selected_id)
    if not record:
        st.error("Record not found.")
        return

    render_history_input_panel(record)
    render_history_output_panel(record)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown(f"### {td('detected_problems', lang)}")
        problems = record.get("detected_problems", [])
        if problems:
            for item in problems:
                st.write(f"- {item}")
        else:
            st.write("- None")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown(f"### {td('likely_causes', lang)}")
        causes = record.get("likely_causes", [])
        if causes:
            for item in causes:
                st.write(f"- {item}")
        else:
            st.write("- None")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown(f"### {td('recommendations', lang)}")
        recommendations = record.get("recommendations", [])
        if recommendations:
            for item in recommendations:
                st.write(f"- {item}")
        else:
            st.write("- None")
        st.markdown("</div>", unsafe_allow_html=True)

        if record.get("notes"):
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            st.markdown(f"### {td('notes', lang)}")
            st.write(record["notes"])
            st.markdown("</div>", unsafe_allow_html=True)
