import pandas as pd
import plotly.express as px
import streamlit as st


def render_cop_chart(inputs: dict) -> None:
    df = pd.DataFrame(
        {
            "Type": ["Actual COP", "Design COP"],
            "COP": [inputs.get("actual_cop", 0.0), inputs.get("design_cop", 0.0)],
        }
    )
    fig = px.bar(df, x="Type", y="COP", title="COP Comparison")
    st.plotly_chart(fig, use_container_width=True)
