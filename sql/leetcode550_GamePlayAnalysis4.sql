
WITH
    total_player_cnt AS (
        SELECT COUNT(DISTINCT player_id) AS total_player FROM Activity
    )

    , player_login AS (
        SELECT
            player_id
            , ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
            , LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS next_day
        FROM Activity
    )

    , rented_players AS (
        SELECT
            COUNT(DISTINCT player_id) AS relogin_player
        FROM player_login
        WHERE rnk = 1 AND DATEDIFF(next_day, event_date) = 1
    )

SELECT ROUND(a.relogin_player/b.total_player, 2) FROM total_player_cnt a, rented_players b
