from datetime import datetime


def build_timestamp_payload() -> dict:
    now = datetime.now()
    return {
        "analysis_date": now.strftime("%Y-%m-%d"),
        "analysis_time": now.strftime("%H:%M:%S"),
        "analysis_month": now.strftime("%B"),
        "analysis_year": now.strftime("%Y"),
        "timestamp": now.isoformat(timespec="seconds"),
    }
