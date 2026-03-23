import streamlit as st
from core.services.export_service import td


def render_alerts_panel(result: dict) -> None:
    lang = st.session_state.get("lang", "dual")

    st.subheader(td("alerts", lang))
    severity = result.get("severity", "info")

    if severity == "critical":
        st.markdown(
            '<span class="status-chip status-critical">CRITICAL / အရေးကြီး</span>',
            unsafe_allow_html=True,
        )
        st.error(td("critical_system_issues", lang))
    elif severity == "warning":
        st.markdown(
            '<span class="status-chip status-warn">WARNING / သတိပေး</span>',
            unsafe_allow_html=True,
        )
        st.warning(td("warning_conditions", lang))
    else:
        st.markdown(
            '<span class="status-chip status-ok">NORMAL / ပုံမှန်</span>',
            unsafe_allow_html=True,
        )
        st.info(td("no_major_warning", lang))

    problems = result.get("problems", [])
    if problems:
        for item in problems:
            st.write(f"- {item}")
    else:
        st.write("- No active problem detected.")

