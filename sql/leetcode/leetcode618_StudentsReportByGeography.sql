
WITH
    student AS (
        SELECT  'Jack' AS name, 'America' AS continent
        UNION ALL
        SELECT 'Pascal' AS name, 'Europe' AS continent
        UNION ALL
        SELECT 'Xi' AS name, 'Asia' AS continent
        UNION ALL
        SELECT 'Jane' AS name, 'America' AS continent
    )

    , ordered_student AS (
        SELECT
            *
            , ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) AS rnk
        FROM student
    )

SELECT
    MIN(CASE WHEN continent = 'America' THEN `name` ELSE NULL END) AS 'America',
    MIN(CASE WHEN continent = 'Asia' THEN `name` ELSE NULL END) AS 'Asia',
    MIN(CASE WHEN continent = 'Europe' THEN `name` ELSE NULL END) AS 'Europe'
FROM 
    ordered_student
GROUP BY rnk