"""Reproduce the SpaceX course-report queries against the included CSV."""
from pathlib import Path
import sqlite3
import pandas as pd

data = Path(__file__).parent / "data" / "Spacex.csv"
with sqlite3.connect(":memory:") as db:
    pd.read_csv(data).to_sql("launches", db, index=False, if_exists="replace")
    queries = {
        "record_count": "SELECT COUNT(*) AS launches FROM launches",
        "launch_sites": "SELECT DISTINCT Launch_Site FROM launches ORDER BY Launch_Site",
        "nasa_payload_kg": "SELECT SUM(PAYLOAD_MASS__KG_) AS total_kg FROM launches WHERE Customer LIKE '%NASA%'",
        "v11_average_payload_kg": "SELECT ROUND(AVG(PAYLOAD_MASS__KG_), 1) AS average_kg FROM launches WHERE Booster_Version LIKE 'F9 v1.1%'",
        "first_ground_landing": "SELECT MIN(Date) AS first_date FROM launches WHERE TRIM(Landing_Outcome) LIKE 'Success (ground pad)%'",
        "mission_outcomes": "SELECT TRIM(Mission_Outcome) AS outcome, COUNT(*) AS launches FROM launches GROUP BY TRIM(Mission_Outcome) ORDER BY launches DESC",
        "maximum_payload_kg": "SELECT MAX(PAYLOAD_MASS__KG_) AS max_kg FROM launches",
    }
    for name, query in queries.items():
        print(f"\n{name}\n{query}")
        print(pd.read_sql_query(query, db).to_string(index=False))
