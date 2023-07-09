
SELECT 
    question_id AS survey_log
FROM (
    SELECT
        question_id, 
        COUNT(answer_id)/COUNT(CASE WHEN action = 'SHOW' THEN 1 ELSE NULl END) AS answer_rate
    FROM survey_log
    GROUP BY question_id
    ORDER BY answer_rate DESC
)
