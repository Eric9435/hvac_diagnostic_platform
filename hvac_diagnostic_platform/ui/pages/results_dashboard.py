import streamlit as st

from ui.components.header import render_hero
from ui.components.kpi_cards import render_kpi_cards
from ui.components.alerts_panel import render_alerts_panel
from ui.components.diagnosis_panel import render_diagnosis_panel
from ui.components.recommendation_panel import render_recommendation_panel
from ui.components.data_quality_panel import render_data_quality_panel
from ui.components.health_score_cards import render_health_score_cards

from ui.charts.temperature_chart import render_temperature_chart
from ui.charts.power_chart import render_power_chart
from ui.charts.cop_chart import render_cop_chart
from ui.charts.cost_chart import render_cost_chart
from ui.charts.waste_chart import render_waste_chart
from ui.charts.trend_chart import render_score_trend_chart

from core.services.export_service import td


def render_input_summary_panel(inputs: dict) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Input Data Record / Input Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### General")
        st.write(f"**Site Name:** {inputs.get('site_name', '-')}")
        st.write(f"**Building Name:** {inputs.get('building_name', '-')}")
        st.write(f"**Equipment Name:** {inputs.get('equipment_name', '-')}")
        st.write(f"**Equipment Tag:** {inputs.get('equipment_tag', '-')}")
        st.write(f"**Operator Name:** {inputs.get('operator_name', '-')}")
        st.write(f"**AC Type:** {inputs.get('ac_type', '-')}")
        st.write(f"**Analysis Mode:** {inputs.get('analysis_mode', '-')}")
        st.write(f"**Date:** {inputs.get('analysis_date', '-')}")
        st.write(f"**Time:** {inputs.get('analysis_time', '-')}")

    with col2:
        st.markdown("### Room / Water Side")
        st.write(f"**Room Temp (°C):** {inputs.get('room_temp', '-')}")
        st.write(f"**Setpoint Temp (°C):** {inputs.get('setpoint_temp', '-')}")
        st.write(f"**Outdoor Temp (°C):** {inputs.get('outdoor_temp', '-')}")
        st.write(f"**CHWS (°C):** {inputs.get('chws', '-')}")
        st.write(f"**CHWR (°C):** {inputs.get('chwr', '-')}")
        st.write(f"**CHW Flow (kg/s):** {inputs.get('chw_flow', '-')}")
        st.write(f"**CWS Entering (°C):** {inputs.get('cws', '-')}")
        st.write(f"**CWS Leaving (°C):** {inputs.get('cwr', '-')}")
        st.write(f"**CW Flow (kg/s):** {inputs.get('cw_flow', '-')}")

    with col3:
        st.markdown("### Equipment / Cost")
        st.write(f"**Chiller Power (kW):** {inputs.get('chiller_power_kw', '-')}")
        st.write(f"**Actual COP (input):** {inputs.get('actual_cop', '-')}")
        st.write(f"**Design COP:** {inputs.get('design_cop', '-')}")
        st.write(f"**AHU Airflow (CFM):** {inputs.get('airflow_cfm', '-')}")
        st.write(f"**Tower Fan Speed (%):** {inputs.get('tower_fan_speed', '-')}")
        st.write(f"**Tower Approach (°C):** {inputs.get('tower_approach', '-')}")
        st.write(f"**Water pH:** {inputs.get('water_ph', '-')}")
        st.write(f"**Water TDS:** {inputs.get('water_tds', '-')}")
        st.write(f"**Water Conductivity:** {inputs.get('water_conductivity', '-')}")
        st.write(f"**Operating Hours:** {inputs.get('operating_hours', '-')}")
        st.write(f"**Tariff:** {inputs.get('tariff', '-')}")

    if inputs.get("notes"):
        st.markdown("### Notes")
        st.write(inputs["notes"])

    st.markdown("</div>", unsafe_allow_html=True)


def render_output_summary_panel(result: dict) -> None:
    st.markdown('<div class="panel-card">', unsafe_allow_html=True)
    st.subheader("Output Summary / Analysis Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Thermal / Performance")
        st.write(f"**CHW Delta-T (°C):** {result.get('delta_t_chw', '-')}")
        st.write(f"**Cooling Output (kW):** {result.get('cooling_kw', '-')}")
        st.write(f"**Actual COP Used:** {result.get('actual_cop_used', '-')}")
        st.write(f"**Ideal Power (kW):** {result.get('ideal_power_kw', '-')}")
        st.write(f"**Total System Power (kW):** {result.get('total_system_power_kw', '-')}")

    with col2:
        st.markdown("### Loss / Cost")
        st.write(f"**Wasted Power (kW):** {result.get('wasted_power_kw', '-')}")
        st.write(f"**Wasted Energy (kWh):** {result.get('wasted_energy_kwh', '-')}")
        st.write(f"**Wasted Cost:** {result.get('wasted_cost', '-')}")
        st.write(f"**Monthly Loss:** {result.get('monthly_loss', '-')}")
        st.write(f"**Annual Loss:** {result.get('annual_loss', '-')}")

    with col3:
        st.markdown("### Status / Score")
        st.write(f"**Comfort Status:** {result.get('comfort_status', '-')}")
        st.write(f"**Efficiency Status:** {result.get('efficiency_status', '-')}")
        st.write(f"**Water Status:** {result.get('water_status', '-')}")
        st.write(f"**Overall Score:** {result.get('overall_score', '-')}")
        st.write(f"**Confidence Score:** {result.get('confidence_score', '-')}")

    st.markdown("</div>", unsafe_allow_html=True)


def render_results_dashboard_page() -> None:
    lang = st.session_state.get("lang", "dual")

    inputs = st.session_state.get("latest_inputs")
    result = st.session_state.get("latest_result")

    if not inputs or not result:
        st.info("No analysis result available yet. Please run a new analysis first.")
        return

    render_hero(
        td("results_dashboard", lang),
        "Premium engineering dashboard for efficiency, diagnostics, scoring, cost-loss analysis, and full input-output record review.",
    )

    render_input_summary_panel(inputs)
    render_output_summary_panel(result)

    st.markdown("---")

    render_kpi_cards(result)
    render_health_score_cards(result)

    left, right = st.columns([1, 1])

    with left:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        render_alerts_panel(result)
        render_diagnosis_panel(result)

        st.subheader(td("root_causes", lang))
        root_causes = result.get("root_causes", [])
        if root_causes:
            for item in root_causes:
                st.write(f"- {item}")
        else:
            st.write("- No root cause inferred.")

        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        render_recommendation_panel(result)
        render_data_quality_panel(result, inputs.get("analysis_mode", "Unknown"))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_temperature_chart(inputs)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_power_chart(inputs, result)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_cop_chart(inputs)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_score_trend_chart(result)
        st.markdown("</div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_cost_chart(result)
        st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_waste_chart(result)
        st.markdown("</div>", unsafe_allow_html=True)


