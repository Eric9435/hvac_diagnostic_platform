from pathlib import Path
import base64
import streamlit as st

from ui.forms.basic_form import render_basic_form
from ui.forms.advanced_form import render_advanced_form
from core.services.timestamp_service import build_timestamp_payload
from core.services.analysis_service import analyze_hvac_data
from storage.repositories.analysis_repository import save_analysis_record
from ui.components.header import render_hero_image


def show_equipment_image(ac_type: str) -> None:
    mapping = {
        "Water-Cooled Chiller": "chiller.jpg",
        "Air-Cooled Chiller": "chiller.jpg",
        "Split AC": "ahu.jpg",
        "VRF": "ahu.jpg",
    }

    img_name = mapping.get(ac_type)
    if not img_name:
        return

    img_path = Path("assets/images") / img_name
    if not img_path.exists():
        return

    encoded = base64.b64encode(img_path.read_bytes()).decode()
    ext = img_path.suffix.lower().replace(".", "")
    if ext == "jpg":
        ext = "jpeg"

    st.markdown(
        f"""
        <div class="panel-card">
            <div class="panel-title">Equipment Preview</div>
            <img src="data:image/{ext};base64,{encoded}" style="width:100%; border-radius:14px;">
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_new_analysis_page() -> None:
    lang = st.session_state.get("lang", "dual")

    render_hero_image(
        "New Analysis / စစ်ဆေးမှုအသစ်",
        "Enter HVAC operating data, run engineering diagnostics, and save the result with timestamp.",
        image_name="hero_hvac.jpg",
    )

    mode = st.radio(
        "Select Analysis Mode / စစ်ဆေးမှုအမျိုးအစားရွေးပါ",
        ["Basic", "Advanced"],
        horizontal=True,
    )

    if mode == "Basic":
        payload = render_basic_form()
    else:
        payload = render_advanced_form()

    if payload:
        show_equipment_image(payload.get("ac_type", ""))

        payload.update(build_timestamp_payload())
        result = analyze_hvac_data(payload)
        full_payload = {**payload, **result}
        analysis_id = save_analysis_record(full_payload)

        st.session_state["latest_inputs"] = payload
        st.session_state["latest_result"] = result
        st.session_state["latest_analysis_id"] = analysis_id

        st.success(f"Analysis completed and saved successfully. Record ID: {analysis_id}")

        st.markdown(
            """
            <div class="panel-card">
                <div class="panel-title">Analysis Summary / စစ်ဆေးမှုအကျဉ်းချုပ်</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Wasted Energy (kWh)", f"{result['wasted_energy_kwh']:.2f}")
        with c2:
            st.metric("Wasted Cost", f"{result['wasted_cost']:.2f}")
        with c3:
            st.metric("Overall Score", f"{result['overall_score']:.1f}")
