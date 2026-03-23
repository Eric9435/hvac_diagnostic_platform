import streamlit as st


def render_power_chart(inputs: dict, result: dict) -> None:
    df = pd.DataFrame(
        {
            "Component": ["Chiller", "CHW Pump", "CW Pump", "Tower Fan", "Wasted Power"],
            "Power (kW)": [
                inputs.get("chiller_power_kw", 0.0),
                inputs.get("chw_pump_kw", 0.0),
                inputs.get("cw_pump_kw", 0.0),
                inputs.get("tower_fan_kw", 0.0),
                result.get("wasted_power_kw", 0.0),
            ],
        }
    )
    fig = px.bar(df, x="Component", y="Power (kW)", title="Power Distribution")
    st.plotly_chart(fig, use_container_width=True)
