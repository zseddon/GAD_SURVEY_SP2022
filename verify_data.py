from db_config import run_query

def count_rows():
    result = run_query("SELECT COUNT(*) AS total FROM gad_survey;")
    print("Total rows:", result[0]["total"])

def missing_values():
    cols = run_query("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = 'gad_survey';
    """)

    for col in cols:
        name = col["column_name"]
        q = f"SELECT COUNT(*) AS missing FROM gad_survey WHERE \"{name}\" IS NULL;"
        result = run_query(q)[0]["missing"]
        print(f"{name}: {result} missing")

def value_ranges():
    nums = ["age", "income", "gad_score"]

    for col in nums:
        q = f"""
        SELECT MIN("{col}") AS min, MAX("{col}") AS max
        FROM gad_survey;
        """
        res = run_query(q)[0]
        print(f"{col}: min={res['min']} max={res['max']}")

if __name__ == "__main__":
    print("\n📊 Data Quality Summary\n")
    count_rows()
    missing_values()
    value_ranges()
