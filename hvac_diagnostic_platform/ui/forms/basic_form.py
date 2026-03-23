import streamlit as st
from config import DEFAULT_TARIFF


def render_basic_form() -> dict | None:
    st.subheader("Basic Analysis Input")

    with st.form("basic_analysis_form", clear_on_submit=False):
        col1, col2 = st.columns(2)

        with col1:
            site_name = st.text_input("Site Name", "Yangon Airport")
            building_name = st.text_input("Building Name", "Terminal Building")
            equipment_name = st.text_input("Equipment Name", "Chiller-01")
            equipment_tag = st.text_input("Equipment Tag", "CH-01")
            operator_name = st.text_input("Operator Name", "Engineer")
            ac_type = st.selectbox("AC Type", ["Water-Cooled Chiller", "Air-Cooled Chiller", "Split AC", "VRF"])

        with col2:
            room_temp = st.number_input("Room Temperature (°C)", value=28.0)
            setpoint_temp = st.number_input("Setpoint Temperature (°C)", value=24.0)
            outdoor_temp = st.number_input("Outdoor Temperature (°C)", value=36.0)
            chws = st.number_input("CHW Supply Temp (°C)", value=7.0)
            chwr = st.number_input("CHW Return Temp (°C)", value=14.0)
            cws = st.number_input("CW Supply Temp (°C)", value=30.0)
            cwr = st.number_input("CW Return Temp (°C)", value=35.0)
            chiller_power_kw = st.number_input("Chiller Power (kW)", value=120.0)
            operating_hours = st.number_input("Operating Hours", value=10.0)
            tariff = st.number_input("Tariff (USD/kWh)", value=float(DEFAULT_TARIFF))

        notes = st.text_area("Observation / Notes", "Room not reaching setpoint.")

        submitted = st.form_submit_button("Run Basic Analysis", use_container_width=True)

        if submitted:
            return {
                "analysis_mode": "Basic",
                "site_name": site_name,
                "building_name": building_name,
                "equipment_name": equipment_name,
                "equipment_tag": equipment_tag,
                "operator_name": operator_name,
                "ac_type": ac_type,
                "room_temp": room_temp,
                "setpoint_temp": setpoint_temp,
                "outdoor_temp": outdoor_temp,
                "chws": chws,
                "chwr": chwr,
                "cws": cws,
                "cwr": cwr,
                "chiller_power_kw": chiller_power_kw,
                "operating_hours": operating_hours,
                "tariff": tariff,
                "actual_cop": 2.8,
                "design_cop": 5.0,
                "notes": notes,
            }

    return None
