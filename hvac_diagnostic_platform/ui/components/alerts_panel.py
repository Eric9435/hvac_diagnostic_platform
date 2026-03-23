import streamlit as st


def render_alerts_panel(result: dict) -> None:
    st.subheader("Alerts")
    severity = result.get("severity", "info")

    if severity == "critical":
        st.error("Critical system issues detected.")
    elif severity == "warning":
        st.warning("Warning conditions detected.")
    else:
        st.info("No major warning detected.")

    for item in result.get("problems", []):
        st.write(f"- {item}")
