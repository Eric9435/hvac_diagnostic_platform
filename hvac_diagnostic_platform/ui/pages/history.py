import streamlit as st
import pandas as pd
from storage.repositories.analysis_repository import fetch_all_analyses, fetch_analysis_by_id
from core.services.export_service import td


def render_history_page() -> None:
    lang = st.session_state.get("lang", "dual")

    st.title(td("history", lang))

    rows = fetch_all_analyses()
    if not rows:
        st.info("No saved analysis records found.")
        return

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)

    st.subheader(td("view_record_details", lang))

    options = {
        f"ID {row['id']} | {row['site_name']} | {row['equipment_name']} | {row['analysis_date']} {row['analysis_time']}": row["id"]
        for row in rows
    }

    selected_label = st.selectbox(td("select_analysis_record", lang), list(options.keys()))
    selected_id = options[selected_label]

    record = fetch_analysis_by_id(selected_id)
    if not record:
        st.error("Record not found.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### {td('general', lang)}")
        st.write(f"**{td('site_name', lang)}:** {record.get('site_name')}")
        st.write(f"**{td('building_name', lang)}:** {record.get('building_name')}")
        st.write(f"**{td('equipment_name', lang)}:** {record.get('equipment_name')}")
        st.write(f"**{td('equipment_tag', lang)}:** {record.get('equipment_tag')}")
        st.write(f"**{td('ac_type', lang)}:** {record.get('ac_type')}")
        st.write(f"**{td('analysis_mode', lang)}:** {record.get('analysis_mode')}")
        st.write(f"**{td('operator_name', lang)}:** {record.get('operator_name')}")
        st.write(f"**{td('date', lang)} / {td('time', lang)}:** {record.get('analysis_date')} {record.get('analysis_time')}")

    with col2:
        st.markdown(f"### {td('kpis', lang)}")
        st.write(f"**{td('wasted_energy', lang)}:** {record.get('wasted_energy_kwh')}")
        st.write(f"**{td('wasted_cost', lang)}:** {record.get('wasted_cost')}")
        st.write(f"**{td('monthly_loss', lang)}:** {record.get('monthly_loss')}")
        st.write(f"**{td('annual_loss', lang)}:** {record.get('annual_loss')}")
        st.write(f"**{td('overall_score', lang)}:** {record.get('overall_score')}")
        st.write(f"**{td('confidence_score', lang)}:** {record.get('confidence_score')}")

    st.markdown(f"### {td('detected_problems', lang)}")
    for item in record.get("detected_problems", []):
        st.write(f"- {item}")

    st.markdown(f"### {td('likely_causes', lang)}")
    for item in record.get("likely_causes", []):
        st.write(f"- {item}")

    st.markdown(f"### {td('recommendations', lang)}")
    for item in record.get("recommendations", []):
        st.write(f"- {item}")

    if record.get("notes"):
        st.markdown(f"### {td('notes', lang)}")
        st.write(record["notes"])
