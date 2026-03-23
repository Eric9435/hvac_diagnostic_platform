import streamlit as st
import pandas as pd
from storage.repositories.analysis_repository import fetch_all_analyses


def render_history_page() -> None:
    st.title("History")

    rows = fetch_all_analyses()
    if not rows:
        st.info("No saved analysis records found.")
        return

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
