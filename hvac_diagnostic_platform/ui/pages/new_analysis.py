import streamlit as st
from ui.forms.basic_form import render_basic_form
from ui.forms.advanced_form import render_advanced_form
from core.services.timestamp_service import build_timestamp_payload
from core.services.analysis_service import analyze_hvac_data
from storage.repositories.analysis_repository import save_analysis_record


def render_new_analysis_page() -> None:
    st.title("New Analysis")

    mode = st.radio("Select Analysis Mode", ["Basic", "Advanced"], horizontal=True)

    if mode == "Basic":
        payload = render_basic_form()
    else:
        payload = render_advanced_form()

    if payload:
        payload.update(build_timestamp_payload())
        result = analyze_hvac_data(payload)
        full_payload = {**payload, **result}
        analysis_id = save_analysis_record(full_payload)

        st.session_state["latest_inputs"] = payload
        st.session_state["latest_result"] = result
        st.session_state["latest_analysis_id"] = analysis_id

        st.success(f"Analysis completed and saved successfully. Record ID: {analysis_id}")
