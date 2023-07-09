WITH temp AS (

SELECT
    user_a, user_b
    , RANK() OVER(ORDER BY no_of_common_followers DESC) AS rnk
FROM (
    SELECT
        a.user_id AS user_a, b.user_id AS user_b
        , COUNT(a.follower_id) AS no_of_common_followers
    FROM Relations a
    JOIN Relations b
    ON
        a.follower_id = b.follower_id
        AND a.user_id < b.user_id
    GROUP BY
        a.user_id, b.user_id
)

)

SELECT 
    user_a, user_b
FROM temp
WHERE rnk = 1