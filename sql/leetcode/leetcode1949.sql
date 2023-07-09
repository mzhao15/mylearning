WITH
    relations AS (
        SELECT user1_id AS user1, user2_id AS user2 FROM Friendship
        UNION ALL
        SELECT user2_id AS user1, user1_id AS user2 FROM Friendship
    )

    , common_friends AS (
        SELECT
            a.user1 AS user_a, b.user1 AS user_b
            , COUNT(DISTINCT a.user2)
        FROM relations a
        JOIN relations b
        ON
            a.user1 < b.user1
            AND a.user2 = b.user2
        GROUP BY a.user1, b.user1
        HAVING COUNT(DISTINCT a.user2) >= 3
    )

SELECT
    *
FROM common_friends