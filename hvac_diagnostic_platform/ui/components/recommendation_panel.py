import streamlit as st


def render_recommendation_panel(result: dict) -> None:
    st.subheader("Recommendations")
    if result.get("recommendations"):
        for idx, item in enumerate(result["recommendations"], start=1):
            st.write(f"{idx}. {item}")
    else:
        st.write("No recommendations generated.")
