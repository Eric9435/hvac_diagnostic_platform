import streamlit as st


def render_input_summary_panel(inputs: dict) -> None:
    st.subheader("Input Data Record / Input Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### General")
        st.write(f"**Site Name:** {inputs.get('site_name', '-')}")
        st.write(f"**Building Name:** {inputs.get('building_name', '-')}")
        st.write(f"**Equipment Name:** {inputs.get('equipment_name', '-')}")
        st.write(f"**Equipment Tag:** {inputs.get('equipment_tag', '-')}")
        st.write(f"**Operator Name:** {inputs.get('operator_name', '-')}")
        st.write(f"**AC Type:** {inputs.get('ac_type', '-')}")

    with col2:
        st.markdown("### Room / Water Side")
        st.write(f"**Room Temp (°C):** {inputs.get('room_temp', '-')}")
        st.write(f"**Setpoint Temp (°C):** {inputs.get('setpoint_temp', '-')}")
        st.write(f"**Outdoor Temp (°C):** {inputs.get('outdoor_temp', '-')}")
        st.write(f"**CHWS (°C):** {inputs.get('chws', '-')}")
        st.write(f"**CHWR (°C):** {inputs.get('chwr', '-')}")
        st.write(f"**CHW Flow (kg/s):** {inputs.get('chw_flow', '-')}")
        st.write(f"**CWS (°C):** {inputs.get('cws', '-')}")
        st.write(f"**CWR (°C):** {inputs.get('cwr', '-')}")
        st.write(f"**CW Flow (kg/s):** {inputs.get('cw_flow', '-')}")

    with col3:
        st.markdown("### Equipment / Cost")
        st.write(f"**Chiller Power (kW):** {inputs.get('chiller_power_kw', '-')}")
        st.write(f"**Actual COP:** {inputs.get('actual_cop', '-')}")
        st.write(f"**Design COP:** {inputs.get('design_cop', '-')}")
        st.write(f"**AHU Airflow (CFM):** {inputs.get('airflow_cfm', '-')}")
        st.write(f"**Tower Fan Speed (%):** {inputs.get('tower_fan_speed', '-')}")
        st.write(f"**Tower Approach (°C):** {inputs.get('tower_approach', '-')}")
        st.write(f"**Water pH:** {inputs.get('water_ph', '-')}")
        st.write(f"**Water TDS:** {inputs.get('water_tds', '-')}")
        st.write(f"**Water Conductivity:** {inputs.get('water_conductivity', '-')}")
        st.write(f"**Operating Hours:** {inputs.get('operating_hours', '-')}")
        st.write(f"**Tariff:** {inputs.get('tariff', '-')}")

    if inputs.get("notes"):
        st.markdown("### Notes")
        st.write(inputs["notes"])
