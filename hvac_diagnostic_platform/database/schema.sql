CREATE TABLE IF NOT EXISTS analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_name TEXT,
    building_name TEXT,
    equipment_name TEXT,
    equipment_tag TEXT,
    ac_type TEXT,
    analysis_mode TEXT,
    operator_name TEXT,
    analysis_date TEXT,
    analysis_time TEXT,
    analysis_month TEXT,
    analysis_year TEXT,
    timestamp TEXT,

    room_temp REAL,
    setpoint_temp REAL,
    outdoor_temp REAL,

    chws REAL,
    chwr REAL,
    cws REAL,
    cwr REAL,

    chiller_power_kw REAL,
    operating_hours REAL,
    tariff REAL,

    actual_cop REAL,
    design_cop REAL,

    chw_flow REAL,
    cw_flow REAL,
    airflow_cfm REAL,

    tower_fan_speed REAL,
    tower_approach REAL,

    water_ph REAL,
    water_tds REAL,
    water_conductivity REAL,

    total_system_power_kw REAL,
    ideal_power_kw REAL,
    wasted_power_kw REAL,
    wasted_energy_kwh REAL,
    wasted_cost REAL,
    monthly_loss REAL,
    annual_loss REAL,

    comfort_status TEXT,
    efficiency_status TEXT,
    overall_score REAL,
    confidence_score REAL,

    detected_problems TEXT,
    likely_causes TEXT,
    recommendations TEXT,
    notes TEXT
);
