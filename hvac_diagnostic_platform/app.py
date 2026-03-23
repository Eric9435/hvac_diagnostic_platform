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
from core.services.export_service import td


st.set_page_config(page_title=APP_TITLE, layout="wide")

SCHEMA_PATH = Path(__file__).resolve().parent / "database" / "schema.sql"
initialize_database(SCHEMA_PATH)

if "lang" not in st.session_state:
    st.session_state["lang"] = "dual"

lang = st.sidebar.selectbox(
    td("language", "dual"),
    options=["en", "my", "dual"],
    format_func=lambda x: {
        "en": "English",
        "my": "မြန်မာ",
        "dual": "English / မြန်မာ",
    }[x],
)

st.session_state["lang"] = lang

st.sidebar.title(td("app_title", lang))
page = st.sidebar.radio(
    "Navigation",
    [
        td("home", lang),
        td("new_analysis", lang),
        td("results_dashboard", lang),
        td("history", lang),
        td("compare", lang),
        td("reports", lang),
        td("settings", lang),
        td("admin", lang),
    ],
)

if page == td("home", lang):
    render_home_page()
elif page == td("new_analysis", lang):
    render_new_analysis_page()
elif page == td("results_dashboard", lang):
    render_results_dashboard_page()
elif page == td("history", lang):
    render_history_page()
elif page == td("compare", lang):
    render_compare_page()
elif page == td("reports", lang):
    render_reports_page()
elif page == td("settings", lang):
    render_settings_page()
elif page == td("admin", lang):
    render_admin_page()

