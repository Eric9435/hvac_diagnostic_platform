import streamlit as st


def render_data_quality_panel(result: dict, mode: str) -> None:
    st.subheader("Data Quality")
    completeness = 65 if mode == "Basic" else 90
    st.write(f"Analysis Mode: {mode}")
    st.write(f"Data Completeness: {completeness}%")
    st.write(f"Diagnosis Confidence: {result['confidence_score']:.1f}%")
