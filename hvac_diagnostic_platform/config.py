from pathlib import Path

APP_TITLE = "HVAC Diagnostic Platform"
APP_SUBTITLE = "HVAC Performance, Energy & Diagnostic Intelligence Platform"

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "database" / "hvac.db"

DEFAULT_CURRENCY = "MMK"
DEFAULT_TARIFF = 900.0
DEFAULT_DESIGN_COP = 5.0

COMFORT_TOLERANCE = 1.0

THRESHOLDS = {
    "tower_fan_speed_low": 80.0,
    "tower_approach_high": 5.0,
    "room_temp_high_offset": 1.0,
    "cop_low_ratio": 0.8,
    "water_tds_high": 1500.0,
    "water_ph_low": 6.5,
    "water_ph_high": 8.5,
    "airflow_low_ratio": 0.85,
}

SEVERITY_COLORS = {
    "info": "blue",
    "warning": "orange",
    "critical": "red",
}
