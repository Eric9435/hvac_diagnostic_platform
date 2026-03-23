import streamlit as st
from config import APP_TITLE, APP_SUBTITLE
from core.services.export_service import td


def render_home_page() -> None:
    lang = st.session_state.get("lang", "dual")

    st.title(td("app_title", lang))
    st.caption(APP_SUBTITLE)

    if lang == "en":
        st.markdown(
            """
            ### Platform Overview
            - Basic Analysis Mode
            - Advanced Engineering Analysis
            - Data Save with Date / Time / Month / Year
            - Dashboard KPIs
            - Diagnosis and Recommendations
            - History Tracking
            """
        )
    elif lang == "my":
        st.markdown(
            """
            ### Platform Overview
            - အခြေခံစစ်ဆေးမှုစနစ်
            - အသေးစိတ်အင်ဂျင်နီယာစစ်ဆေးမှု
            - ရက်စွဲ / အချိန် / လ / နှစ် ဖြင့် data သိမ်းဆည်းခြင်း
            - Dashboard KPI များ
            - Diagnosis နှင့် Recommendation
            - History Tracking
            """
        )
    else:
        st.markdown(
            """
            ### Platform Overview / ပလက်ဖောင်းအကျဉ်းချုပ်
            - Basic Analysis Mode / အခြေခံစစ်ဆေးမှုစနစ်
            - Advanced Engineering Analysis / အသေးစိတ်အင်ဂျင်နီယာစစ်ဆေးမှု
            - Data Save with Date / Time / Month / Year / ရက်စွဲ၊ အချိန်၊ လ၊ နှစ်ဖြင့် သိမ်းဆည်းခြင်း
            - Dashboard KPIs / Dashboard KPI များ
            - Diagnosis and Recommendations / Diagnosis နှင့် Recommendation
            - History Tracking / မှတ်တမ်းစောင့်ကြည့်မှု
            """
        )

