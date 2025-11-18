import pandas as pd

CSV_PATH = "data/gad_survey_data.csv"
TABLE_NAME = "gad_survey"

def infer_type(series):
    if pd.api.types.is_integer_dtype(series):
        return "INTEGER"
    if pd.api.types.is_float_dtype(series):
        return "FLOAT"
    return "TEXT"

def generate_schema():
    df = pd.read_csv(CSV_PATH)
    schema = []

    for col in df.columns:
        sql_type = infer_type(df[col])
        schema.append(f'    "{col}" {sql_type}')

    create_sql = f"CREATE TABLE {TABLE_NAME} (\n" + ",\n".join(schema) + "\n);\n"
    print(create_sql)

    with open("schema/auto_create_tables.sql", "w") as f:
        f.write(create_sql)

    print("✅ Saved to schema/auto_create_tables.sql")

if __name__ == "__main__":
    generate_schema()
