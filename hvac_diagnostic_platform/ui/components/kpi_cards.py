import streamlit as st


def render_kpi_cards(result: dict) -> None:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total System Power (kW)", f"{result['total_system_power_kw']:.2f}")
    c2.metric("Wasted Energy (kWh)", f"{result['wasted_energy_kwh']:.2f}")
    c3.metric("Wasted Cost", f"{result['wasted_cost']:.2f}")
    c4.metric("Overall Score", f"{result['overall_score']:.1f}")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Ideal Power (kW)", f"{result['ideal_power_kw']:.2f}")
    c6.metric("Wasted Power (kW)", f"{result['wasted_power_kw']:.2f}")
    c7.metric("Confidence", f"{result['confidence_score']:.1f}%")
    c8.metric("Water Health", f"{result['water_health_score']:.1f}")
