

-- Method 1
SELECT
    player_id, event_date,
    SUM(games_played) OVER(PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
FROM Activity
ORDER BY player_id, event_date

-- Method 2
SELECT
    a.player_id, a.event_date,
    SUM(b.games_played) AS games_played_so_far
FROM Activity a, Activity b
WHERE a.player_id = b.player_id
    AND a.event_date >= b.event_date
GROUP BY
    a.player_id, a.event_date
