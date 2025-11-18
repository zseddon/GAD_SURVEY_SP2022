import pandas as pd
import psycopg2
from db_config import get_connection

TABLE_NAME = "gad_survey"
CSV_PATH = "data/gad_survey_data.csv"
CHUNK_SIZE = 1000

def load_csv():
    conn = get_connection()
    cur = conn.cursor()

    for chunk in pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE):
        cols = ", ".join(f'"{c}"' for c in chunk.columns)
        placeholders = ", ".join(["%s"] * len(chunk.columns))

        for _, row in chunk.iterrows():
            values = [None if pd.isna(v) else v for v in row.values]
            query = f"INSERT INTO {TABLE_NAME} ({cols}) VALUES ({placeholders})"
            try:
                cur.execute(query, values)
            except Exception as e:
                print("❌ Error inserting row:", row.to_dict())
                print("   →", e)
                conn.rollback()
                continue

        conn.commit()

    cur.close()
    conn.close()
    print("✅ CSV data loaded successfully.")

if __name__ == "__main__":
    load_csv()
