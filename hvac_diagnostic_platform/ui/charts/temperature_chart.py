import pandas as pd
import plotly.express as px
import streamlit as st


def render_temperature_chart(inputs: dict) -> None:
    df = pd.DataFrame(
        {
            "Metric": ["Room Temperature", "Setpoint", "Outdoor Temperature", "CHWS", "CHWR", "CWS", "CWR"],
            "Value": [
                inputs.get("room_temp", 0.0),
                inputs.get("setpoint_temp", 0.0),
                inputs.get("outdoor_temp", 0.0),
                inputs.get("chws", 0.0),
                inputs.get("chwr", 0.0),
                inputs.get("cws", 0.0),
                inputs.get("cwr", 0.0),
            ],
        }
    )
    fig = px.bar(df, x="Metric", y="Value", title="Temperature Snapshot")
    st.plotly_chart(fig, use_container_width=True)
