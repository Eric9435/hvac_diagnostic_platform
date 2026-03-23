import pandas as pd
import plotly.express as px
import streamlit as st


def render_waste_chart(result: dict) -> None:
    df = pd.DataFrame(
        {
            "Type": ["Ideal Power", "Actual Waste"],
            "kW": [result.get("ideal_power_kw", 0.0), result.get("wasted_power_kw", 0.0)],
        }
    )
    fig = px.pie(df, names="Type", values="kW", title="Ideal vs Wasted Power")
    st.plotly_chart(fig, use_container_width=True)
