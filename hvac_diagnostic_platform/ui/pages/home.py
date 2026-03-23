import streamlit as st
from config import APP_SUBTITLE
from core.services.export_service import td
from ui.components.header import render_hero_image, render_icon_card


def render_home_page() -> None:
    lang = st.session_state.get("lang", "dual")

    if lang == "en":
        title = "HVAC Diagnostic Platform"
        subtitle = (
            "A premium engineering dashboard for HVAC efficiency diagnostics, "
            "energy loss analysis, root-cause detection, and decision-ready reporting."
        )
    elif lang == "my":
        title = "HVAC စနစ် စစ်ဆေးမှု ပလက်ဖောင်း"
        subtitle = (
            "HVAC ထိရောက်မှု စစ်ဆေးခြင်း၊ စွမ်းအင်ဆုံးရှုံးမှု တွက်ချက်ခြင်း၊ "
            "အကြောင်းရင်းရှာဖွေခြင်းနှင့် အင်ဂျင်နီယာအစီရင်ခံစာများအတွက် premium dashboard ဖြစ်ပါသည်။"
        )
    else:
        title = "HVAC Diagnostic Platform / HVAC စနစ် စစ်ဆေးမှု ပလက်ဖောင်း"
        subtitle = (
            "A premium engineering dashboard for HVAC efficiency diagnostics, energy loss analysis, "
            "root-cause detection, and decision-ready reporting. "
            "HVAC ထိရောက်မှု စစ်ဆေးခြင်း၊ စွမ်းအင်ဆုံးရှုံးမှု တွက်ချက်ခြင်းနှင့် "
            "အကြောင်းရင်းရှာဖွေခြင်းအတွက် premium dashboard ဖြစ်ပါသည်။"
        )

    render_hero_image(title, subtitle, image_name="hero_hvac.jpg")
    st.caption(APP_SUBTITLE)

    st.markdown("### System Modules / စနစ်အပိုင်းများ")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_icon_card("Chiller", "chiller.png")
    with c2:
        render_icon_card("Cooling Tower", "tower.png")
    with c3:
        render_icon_card("Pump", "pump.png")
    with c4:
        render_icon_card("AHU / Airflow", "ahu.png")

    st.markdown("---")

    if lang == "en":
        st.markdown(
            """
            ### Platform Overview
            - Basic Analysis Mode
            - Advanced Engineering Analysis
            - Timestamped Data Save
            - KPI Dashboard
            - Diagnostics and Recommendations
            - History and Comparison
            """
        )
    elif lang == "my":
        st.markdown(
            """
            ### Platform Overview
            - အခြေခံစစ်ဆေးမှုစနစ်
            - အသေးစိတ် အင်ဂျင်နီယာစစ်ဆေးမှု
            - အချိန်နှင့်တပြေးညီ data သိမ်းဆည်းခြင်း
            - KPI Dashboard
            - Diagnosis နှင့် Recommendation
            - History နှင့် Comparison
            """
        )
    else:
        st.markdown(
            """
            ### Platform Overview / ပလက်ဖောင်းအကျဉ်းချုပ်
            - Basic Analysis Mode / အခြေခံစစ်ဆေးမှုစနစ်  
            - Advanced Engineering Analysis / အသေးစိတ် အင်ဂျင်နီယာစစ်ဆေးမှု  
            - Timestamped Data Save / အချိန်နှင့်တပြေးညီ data သိမ်းဆည်းခြင်း  
            - KPI Dashboard / KPI Dashboard  
            - Diagnostics and Recommendations / Diagnosis နှင့် Recommendation  
            - History and Comparison / History နှင့် Comparison  
            """
        )



