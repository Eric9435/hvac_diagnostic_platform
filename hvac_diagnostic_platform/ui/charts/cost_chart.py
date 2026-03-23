import pandas as pd
import plotly.express as px
import streamlit as st


def render_cost_chart(result: dict) -> None:
    df = pd.DataFrame(
        {
            "Period": ["Daily Waste", "Monthly Waste", "Annual Waste"],
            "Cost": [
                result.get("wasted_cost", 0.0),
                result.get("monthly_loss", 0.0),
                result.get("annual_loss", 0.0),
            ],
        }
    )
    fig = px.bar(df, x="Period", y="Cost", title="Estimated Cost Loss")
    st.plotly_chart(fig, use_container_width=True)
