import pandas as pd
import plotly.express as px
import streamlit as st


def render_score_trend_chart(result: dict) -> None:
    df = pd.DataFrame(
        {
            "Subsystem": ["Chiller", "Tower", "AHU", "Water", "Overall"],
            "Score": [
                result.get("chiller_score", 0),
                result.get("tower_score", 0),
                result.get("ahu_score", 0),
                result.get("water_health_score", 0),
                result.get("overall_score", 0),
            ],
        }
    )
    fig = px.bar(df, x="Subsystem", y="Score", title="Subsystem Health Score Overview")
    st.plotly_chart(fig, use_container_width=True)
