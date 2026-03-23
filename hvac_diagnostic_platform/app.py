from pathlib import Path
import streamlit as st

from config import APP_TITLE
from storage.db import initialize_database
from ui.pages.home import render_home_page
from ui.pages.new_analysis import render_new_analysis_page
from ui.pages.results_dashboard import render_results_dashboard_page
from ui.pages.history import render_history_page
from ui.pages.compare import render_compare_page
from ui.pages.reports import render_reports_page
from ui.pages.settings import render_settings_page
from ui.pages.admin import render_admin_page


st.set_page_config(page_title=APP_TITLE, layout="wide")

SCHEMA_PATH = Path(__file__).resolve().parent / "database" / "schema.sql"
initialize_database(SCHEMA_PATH)

st.sidebar.title("HVAC Diagnostic Platform")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "New Analysis", "Results Dashboard", "History", "Compare", "Reports", "Settings", "Admin"],
)

if page == "Home":
    render_home_page()
elif page == "New Analysis":
    render_new_analysis_page()
elif page == "Results Dashboard":
    render_results_dashboard_page()
elif page == "History":
    render_history_page()
elif page == "Compare":
    render_compare_page()
elif page == "Reports":
    render_reports_page()
elif page == "Settings":
    render_settings_page()
elif page == "Admin":
    render_admin_page()
