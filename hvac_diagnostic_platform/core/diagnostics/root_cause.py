def infer_root_causes(all_causes: list[str]) -> list[str]:
    text = " ".join(all_causes).lower()
    root_causes = []

    if "tower airflow" in text or "heat rejection" in text:
        root_causes.append("Cooling tower performance degradation is a major probable root cause.")

    if "water quality" in text or "scaling" in text or "fouling" in text:
        root_causes.append("Water treatment / fouling issue is a major probable root cause.")

    if "air delivery" in text or "airflow" in text or "filter" in text:
        root_causes.append("AHU/airflow-side restriction is a major probable root cause.")

    if "excess power" in text or "cop" in text:
        root_causes.append("Chiller efficiency degradation is a major probable root cause.")

    unique = []
    for item in root_causes:
        if item not in unique:
            unique.append(item)
    return unique
