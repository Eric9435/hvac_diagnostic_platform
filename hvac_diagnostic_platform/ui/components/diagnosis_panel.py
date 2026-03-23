import streamlit as st


def render_diagnosis_panel(result: dict) -> None:
    st.subheader("Likely Causes")
    if result.get("causes"):
        for item in result["causes"]:
            st.write(f"- {item}")
    else:
        st.write("No likely causes generated.")
