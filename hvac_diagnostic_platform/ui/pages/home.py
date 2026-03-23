import streamlit as st
from config import APP_TITLE, APP_SUBTITLE


def render_home_page() -> None:
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)
    st.markdown(
        """
        ### Platform Overview
        - Basic Analysis Mode
        - Advanced Engineering Analysis
        - Data Save with Date / Time / Month / Year
        - Dashboard KPIs
        - Diagnosis and Recommendations
        - History Tracking
        """
    )
