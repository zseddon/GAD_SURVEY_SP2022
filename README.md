# GAD Survey SQL Repository

This repository contains a SQL schema and import instructions for the GAD survey dataset.

## Files
- `schema/create_tables.sql` — Generated table schema based on the CSV.
- `data/gad_survey_data.csv` — Source dataset.
- `scripts/import_data.sql` — COPY command to load data into PostgreSQL.

## How to Use
1. Create a PostgreSQL database:
   ```
   createdb gad_db
   ```
2. Run schema:
   ```
   psql gad_db -f schema/create_tables.sql
   ```
3. Import data:
   ```
   psql gad_db -f scripts/import_data.sql
   ```

