import streamlit as st


def render_health_score_cards(result: dict) -> None:
    st.subheader("Subsystem Health Scores")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Chiller Score", f"{result.get('chiller_score', 0):.1f}/100")
    c2.metric("Tower Score", f"{result.get('tower_score', 0):.1f}/100")
    c3.metric("AHU Score", f"{result.get('ahu_score', 0):.1f}/100")
    c4.metric("Water Score", f"{result.get('water_health_score', 0):.1f}/100")
