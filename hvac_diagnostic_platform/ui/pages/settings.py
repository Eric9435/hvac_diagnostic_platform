import streamlit as st
from config import DEFAULT_TARIFF, DEFAULT_DESIGN_COP


def render_settings_page() -> None:
    st.title("Settings")
    st.write(f"Default Tariff: {DEFAULT_TARIFF}")
    st.write(f"Default Design COP: {DEFAULT_DESIGN_COP}")
