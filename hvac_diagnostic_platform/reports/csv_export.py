import io
import pandas as pd


def build_record_csv_bytes(record: dict) -> bytes:
    flat_record = record.copy()

    for key in ["detected_problems", "likely_causes", "recommendations"]:
        value = flat_record.get(key)
        if isinstance(value, list):
            flat_record[key] = " | ".join(value)

    df = pd.DataFrame([flat_record])
    output = io.StringIO()
    df.to_csv(output, index=False)
    return output.getvalue().encode("utf-8")
