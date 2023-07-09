

WITH
    event_avg AS (
        SELECT
            event_type, AVG(occurences) AS avg_occ
        FROM Events
        GROUP BY event_type
    )

SELECT
    a.business_id, COUNT(1)
FROM Events a 
JOIN evente_avg b
ON a.event_type = b.event_type
WHERE a.occurences > avg_occ
GROUP BY business_id
HAVING COUNT(1) > 1
