import streamlit as st
from ui.components.kpi_cards import render_kpi_cards
from ui.components.alerts_panel import render_alerts_panel
from ui.components.diagnosis_panel import render_diagnosis_panel
from ui.components.recommendation_panel import render_recommendation_panel
from ui.components.data_quality_panel import render_data_quality_panel
from ui.charts.temperature_chart import render_temperature_chart
from ui.charts.power_chart import render_power_chart
from ui.charts.cop_chart import render_cop_chart
from ui.charts.cost_chart import render_cost_chart
from ui.charts.waste_chart import render_waste_chart


def render_results_dashboard_page() -> None:
    st.title("Results Dashboard")

    inputs = st.session_state.get("latest_inputs")
    result = st.session_state.get("latest_result")

    if not inputs or not result:
        st.info("No analysis result available yet. Please run a new analysis first.")
        return

    render_kpi_cards(result)

    c1, c2 = st.columns(2)
    with c1:
        render_alerts_panel(result)
        render_diagnosis_panel(result)
    with c2:
        render_recommendation_panel(result)
        render_data_quality_panel(result, inputs["analysis_mode"])

    render_temperature_chart(inputs)
    render_power_chart(inputs, result)
    render_cop_chart(inputs)
    render_cost_chart(result)
    render_waste_chart(result)
