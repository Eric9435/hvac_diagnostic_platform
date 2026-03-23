import streamlit as st
from core.services.export_service import td


def render_alerts_panel(result: dict) -> None:
    lang = st.session_state.get("lang", "dual")

    st.subheader(td("alerts", lang))
    severity = result.get("severity", "info")

    if severity == "critical":
        st.error(td("critical_system_issues", lang))
    elif severity == "warning":
        st.warning(td("warning_conditions", lang))
    else:
        st.info(td("no_major_warning", lang))

    for item in result.get("problems", []):
        st.write(f"- {item}")

