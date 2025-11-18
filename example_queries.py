from db_config import run_query

def top_gad_scores(limit=10):
    q = f"""
    SELECT respondent_id, gad_score, age, gender
    FROM gad_survey
    ORDER BY gad_score DESC
    LIMIT {limit};
    """
    return run_query(q)

def average_scores_by_country():
    q = """
    SELECT country, AVG(gad_score) AS avg_score
    FROM gad_survey
    GROUP BY country
    ORDER BY avg_score DESC;
    """
    return run_query(q)

if __name__ == "__main__":
    print(top_gad_scores())
    print(average_scores_by_country())
