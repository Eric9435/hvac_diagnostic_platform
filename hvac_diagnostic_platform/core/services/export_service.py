TEXTS = {
    "en": {
        "app_title": "HVAC Diagnostic Platform",
        "home": "Home",
        "new_analysis": "New Analysis",
        "results_dashboard": "Results Dashboard",
        "history": "History",
        "compare": "Compare",
        "reports": "Reports",
        "settings": "Settings",
        "admin": "Admin",
        "language": "Language",
        "english": "English",
        "myanmar": "Myanmar",
        "dual": "Dual",
        "site_name": "Site Name",
        "building_name": "Building Name",
        "equipment_name": "Equipment Name",
        "equipment_tag": "Equipment Tag",
        "ac_type": "AC Type",
        "analysis_mode": "Analysis Mode",
        "operator_name": "Operator Name",
        "date": "Date",
        "time": "Time",
        "room_temp": "Room Temperature",
        "setpoint_temp": "Setpoint Temperature",
        "outdoor_temp": "Outdoor Temperature",
        "actual_cop": "Actual COP",
        "design_cop": "Design COP",
        "total_system_power": "Total System Power",
        "wasted_energy": "Wasted Energy (kWh)",
        "wasted_cost": "Wasted Cost",
        "monthly_loss": "Monthly Loss",
        "annual_loss": "Annual Loss",
        "comfort_status": "Comfort Status",
        "efficiency_status": "Efficiency Status",
        "overall_score": "Overall Score",
        "confidence_score": "Confidence Score",
        "detected_problems": "Detected Problems",
        "likely_causes": "Likely Causes",
        "recommendations": "Recommendations",
        "notes": "Notes",
        "executive_summary": "HVAC Diagnostic Executive Summary",
        "general": "General",
        "kpis": "KPIs",
        "view_record_details": "View Record Details",
        "select_analysis_record": "Select analysis record",
        "download_summary_txt": "Download Summary as TXT",
        "download_record_csv": "Download Record as CSV",
        "subsystem_health_scores": "Subsystem Health Scores",
        "root_causes": "Root Causes",
        "alerts": "Alerts",
        "critical_system_issues": "Critical system issues detected.",
        "warning_conditions": "Warning conditions detected.",
        "no_major_warning": "No major warning detected.",
    },
    "my": {
        "app_title": "HVAC စနစ် စစ်ဆေးမှု ပလက်ဖောင်း",
        "home": "ပင်မစာမျက်နှာ",
        "new_analysis": "စစ်ဆေးမှုအသစ်",
        "results_dashboard": "ရလဒ်ဒက်ရှ်ဘုတ်",
        "history": "မှတ်တမ်းများ",
        "compare": "နှိုင်းယှဉ်ခြင်း",
        "reports": "အစီရင်ခံစာများ",
        "settings": "ဆက်တင်များ",
        "admin": "အုပ်ချုပ်မှု",
        "language": "ဘာသာစကား",
        "english": "အင်္ဂလိပ်",
        "myanmar": "မြန်မာ",
        "dual": "နှစ်ဘာသာ",
        "site_name": "နေရာအမည်",
        "building_name": "အဆောက်အဦးအမည်",
        "equipment_name": "စက်ပစ္စည်းအမည်",
        "equipment_tag": "စက်နံပါတ်/Tag",
        "ac_type": "အဲကွန်းအမျိုးအစား",
        "analysis_mode": "စစ်ဆေးမှုအမျိုးအစား",
        "operator_name": "စစ်ဆေးသူအမည်",
        "date": "ရက်စွဲ",
        "time": "အချိန်",
        "room_temp": "အခန်းအပူချိန်",
        "setpoint_temp": "သတ်မှတ်အပူချိန်",
        "outdoor_temp": "ပြင်ပအပူချိန်",
        "actual_cop": "Actual COP",
        "design_cop": "Design COP",
        "total_system_power": "စုစုပေါင်းစနစ်ပါဝါ",
        "wasted_energy": "အလကားကုန်သွားသောစွမ်းအင် (kWh)",
        "wasted_cost": "ဆုံးရှုံးငွေ",
        "monthly_loss": "လစဉ်ဆုံးရှုံးမှု",
        "annual_loss": "နှစ်စဉ်ဆုံးရှုံးမှု",
        "comfort_status": "သက်တောင့်သက်သာအခြေအနေ",
        "efficiency_status": "ထိရောက်မှုအခြေအနေ",
        "overall_score": "စုစုပေါင်းရမှတ်",
        "confidence_score": "ယုံကြည်နိုင်မှုရမှတ်",
        "detected_problems": "တွေ့ရှိသောပြဿနာများ",
        "likely_causes": "ဖြစ်နိုင်သောအကြောင်းရင်းများ",
        "recommendations": "အကြံပြုချက်များ",
        "notes": "မှတ်စုများ",
        "executive_summary": "HVAC စနစ် စစ်ဆေးမှု အကျဉ်းချုပ်",
        "general": "အထွေထွေ",
        "kpis": "အဓိကညွှန်းကိန်းများ",
        "view_record_details": "မှတ်တမ်းအသေးစိတ်ကြည့်ရန်",
        "select_analysis_record": "စစ်ဆေးမှုမှတ်တမ်းရွေးပါ",
        "download_summary_txt": "TXT အဖြစ် download လုပ်ရန်",
        "download_record_csv": "CSV အဖြစ် download လုပ်ရန်",
        "subsystem_health_scores": "Subsystem ရမှတ်များ",
        "root_causes": "အဓိကအကြောင်းရင်းများ",
        "alerts": "သတိပေးချက်များ",
        "critical_system_issues": "စနစ်တွင် အရေးကြီးပြဿနာများ တွေ့ရှိထားသည်။",
        "warning_conditions": "သတိထားရမည့် အခြေအနေများ တွေ့ရှိထားသည်။",
        "no_major_warning": "အရေးကြီး သတိပေးချက် မရှိသေးပါ။",
    },
}


def get_text(key: str, lang: str = "en") -> str:
    return TEXTS.get(lang, TEXTS["en"]).get(key, key)


def t(key: str, lang: str = "en") -> str:
    return get_text(key, lang)


def td(key: str, lang: str = "en") -> str:
    """
    Dual language text
    """
    en = TEXTS["en"].get(key, key)
    my = TEXTS["my"].get(key, key)
    if lang == "en":
        return en
    if lang == "my":
        return my
    return f"{en} / {my}"


