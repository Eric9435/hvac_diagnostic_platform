import streamlit as st


def render_kpi_cards(result: dict) -> None:
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total System Power (kW)", f"{result['total_system_power_kw']:.2f}")
    with c2:
        st.metric("Wasted Energy (kWh)", f"{result['wasted_energy_kwh']:.2f}")
    with c3:
        st.metric("Wasted Cost", f"{result['wasted_cost']:.2f}")
    with c4:
        st.metric("Overall Score", f"{result['overall_score']:.1f}")

    c5, c6, c7, c8 = st.columns(4)
    with c5:
        st.metric("Ideal Power (kW)", f"{result['ideal_power_kw']:.2f}")
    with c6:
        st.metric("Wasted Power (kW)", f"{result['wasted_power_kw']:.2f}")
    with c7:
        st.metric("Confidence", f"{result['confidence_score']:.1f}%")
    with c8:
        st.metric("Water Health", f"{result['water_health_score']:.1f}")
