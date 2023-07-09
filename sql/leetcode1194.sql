

SELECT
    t1.group_id, t.player_id
FROM (
    SELECT 
        t.group_id,
        t.player_id,
        ROW_NUMBER() OVER(PARTITION BY t.group_id ORDER BY SUM(t.score) DESC, t.player_id) AS rnk
    FROM (
        SELECT 
            b.group_id,
            b.player_id,
            a.first_score AS score
        FROM Matches a
        JOIN Players b
        ON a.first_player = b.player_id

        UNION ALL

        SELECT 
            b.group_id,
            b.player_id,
            a.second_score AS score
        FROM Matches a
        JOIN Players b
        ON a.second_player = b.player_id
    ) t
) t1
WHERE t1.rnk = 1
