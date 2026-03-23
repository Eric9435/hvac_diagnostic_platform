import streamlit as st
from storage.repositories.analysis_repository import fetch_all_analyses, fetch_analysis_by_id
from reports.report_builder import build_executive_summary
from reports.csv_export import build_record_csv_bytes
from core.services.export_service import td


def render_reports_page() -> None:
    lang = st.session_state.get("lang", "dual")

    st.title(td("reports", lang))

    rows = fetch_all_analyses()
    if not rows:
        st.info("No saved analysis records available for reporting.")
        return

    options = {
        f"ID {row['id']} | {row['site_name']} | {row['equipment_name']} | {row['analysis_date']} {row['analysis_time']}": row["id"]
        for row in rows
    }

    selected_label = st.selectbox(td("select_analysis_record", lang), list(options.keys()))
    selected_id = options[selected_label]

    record = fetch_analysis_by_id(selected_id)
    if not record:
        st.error("Selected record could not be loaded.")
        return

    summary_text = build_executive_summary(record, lang=lang)

    st.subheader(td("executive_summary", lang))
    st.text(summary_text)

    st.download_button(
        label=td("download_summary_txt", lang),
        data=summary_text.encode("utf-8"),
        file_name=f"hvac_report_{selected_id}.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.download_button(
        label=td("download_record_csv", lang),
        data=build_record_csv_bytes(record),
        file_name=f"hvac_record_{selected_id}.csv",
        mime="text/csv",
        use_container_width=True,
    )

