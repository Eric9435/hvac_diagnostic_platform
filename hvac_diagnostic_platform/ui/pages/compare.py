import streamlit as st
import pandas as pd
import plotly.express as px
from storage.repositories.analysis_repository import fetch_all_analyses


def render_compare_page() -> None:
    st.title("Compare Analyses")

    rows = fetch_all_analyses()
    if len(rows) < 2:
        st.info("At least two saved records are required for comparison.")
        return

    df = pd.DataFrame(rows)

    record_options = {
        f"ID {row['id']} | {row['site_name']} | {row['equipment_name']} | {row['analysis_date']} {row['analysis_time']}": row["id"]
        for row in rows
    }

    col1, col2 = st.columns(2)
    with col1:
        label_a = st.selectbox("Select Record A", list(record_options.keys()), index=0)
    with col2:
        label_b = st.selectbox("Select Record B", list(record_options.keys()), index=min(1, len(record_options) - 1))

    id_a = record_options[label_a]
    id_b = record_options[label_b]

    row_a = df[df["id"] == id_a].iloc[0]
    row_b = df[df["id"] == id_b].iloc[0]

    compare_df = pd.DataFrame(
        {
            "Metric": [
                "Wasted Energy (kWh)",
                "Wasted Cost",
                "Overall Score",
                "Confidence Score",
            ],
            "Record A": [
                row_a["wasted_energy_kwh"],
                row_a["wasted_cost"],
                row_a["overall_score"],
                row_a["confidence_score"],
            ],
            "Record B": [
                row_b["wasted_energy_kwh"],
                row_b["wasted_cost"],
                row_b["overall_score"],
                row_b["confidence_score"],
            ],
        }
    )

    st.dataframe(compare_df, use_container_width=True)

    plot_df = compare_df.melt(id_vars="Metric", var_name="Record", value_name="Value")
    fig = px.bar(plot_df, x="Metric", y="Value", color="Record", barmode="group", title="Comparison Overview")
    st.plotly_chart(fig, use_container_width=True)
