import streamlit as st
from config import DEFAULT_TARIFF, DEFAULT_DESIGN_COP


def render_advanced_form() -> dict | None:
    st.subheader("Advanced Analysis Input")

    with st.form("advanced_analysis_form", clear_on_submit=False):
        st.markdown("### General Information")
        c1, c2, c3 = st.columns(3)
        with c1:
            site_name = st.text_input("Site Name", "Yangon Airport")
            building_name = st.text_input("Building Name", "Terminal Building")
            equipment_name = st.text_input("Equipment Name", "Chiller-01")
        with c2:
            equipment_tag = st.text_input("Equipment Tag", "CH-01")
            operator_name = st.text_input("Operator Name", "Engineer")
            ac_type = st.selectbox("AC Type", ["Water-Cooled Chiller", "Air-Cooled Chiller", "Split AC", "VRF"])
        with c3:
            room_temp = st.number_input("Room Temp (°C)", value=28.0)
            setpoint_temp = st.number_input("Setpoint (°C)", value=24.0)
            outdoor_temp = st.number_input("Outdoor Temp (°C)", value=36.0)

        st.markdown("### Chiller / Water Side")
        c1, c2, c3 = st.columns(3)
        with c1:
            chws = st.number_input("CHWS (°C)", value=7.0)
            chwr = st.number_input("CHWR (°C)", value=14.0)
            chw_flow = st.number_input("CHW Flow", value=20.0)
        with c2:
            cws = st.number_input("CWS Entering (°C)", value=30.0)
            cwr = st.number_input("CWS Leaving (°C)", value=35.0)
            cw_flow = st.number_input("CW Flow", value=22.0)
        with c3:
            chiller_power_kw = st.number_input("Chiller Power (kW)", value=120.0)
            actual_cop = st.number_input("Actual COP", value=2.8)
            design_cop = st.number_input("Design COP", value=float(DEFAULT_DESIGN_COP))

        st.markdown("### Air / Tower / Water Treatment")
        c1, c2, c3 = st.columns(3)
        with c1:
            airflow_cfm = st.number_input("AHU Airflow (CFM)", value=8500.0)
            tower_fan_speed = st.number_input("Tower Fan Speed (%)", value=65.0)
            tower_approach = st.number_input("Tower Approach (°C)", value=6.0)
        with c2:
            chw_pump_kw = st.number_input("CHW Pump Power (kW)", value=15.0)
            cw_pump_kw = st.number_input("CW Pump Power (kW)", value=18.0)
            tower_fan_kw = st.number_input("Tower Fan Power (kW)", value=10.0)
        with c3:
            water_ph = st.number_input("Water pH", value=9.1)
            water_tds = st.number_input("Water TDS", value=2100.0)
            water_conductivity = st.number_input("Water Conductivity", value=2500.0)

        st.markdown("### Operating / Cost")
        c1, c2 = st.columns(2)
        with c1:
            operating_hours = st.number_input("Operating Hours", value=10.0)
        with c2:
            tariff = st.number_input("Tariff (USD/kWh)", value=float(DEFAULT_TARIFF))

        notes = st.text_area("Observation / Notes", "Dirty filter and poor cooling tower performance suspected.")

        submitted = st.form_submit_button("Run Advanced Analysis", use_container_width=True)

        if submitted:
            return {
                "analysis_mode": "Advanced",
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
                "chw_flow": chw_flow,
                "cws": cws,
                "cwr": cwr,
                "cw_flow": cw_flow,
                "chiller_power_kw": chiller_power_kw,
                "actual_cop": actual_cop,
                "design_cop": design_cop,
                "airflow_cfm": airflow_cfm,
                "tower_fan_speed": tower_fan_speed,
                "tower_approach": tower_approach,
                "chw_pump_kw": chw_pump_kw,
                "cw_pump_kw": cw_pump_kw,
                "tower_fan_kw": tower_fan_kw,
                "water_ph": water_ph,
                "water_tds": water_tds,
                "water_conductivity": water_conductivity,
                "operating_hours": operating_hours,
                "tariff": tariff,
                "notes": notes,
            }

    return None
