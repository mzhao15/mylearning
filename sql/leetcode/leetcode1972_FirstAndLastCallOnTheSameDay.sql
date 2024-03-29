/**
https://circlecoder.com/first-and-last-call-on-the-same-day/

Table: Calls
+--------------+----------+
| Column Name  | Type     |
+--------------+----------+
| caller_id    | int      |
| recipient_id | int      |
| call_time    | datetime |
+--------------+----------+
(caller_id, recipient_id, call_time) is the primary key for this table.
Each row contains information about the time of a phone call between caller_id and recipient_id.

Write an SQL query to report the IDs of the users whose first and last calls on any day were with the same person. Calls are counted regardless of being the caller or the recipient.

Return the result table in any order.

The query result format is in the following example:

Calls table:
+-----------+--------------+---------------------+
| caller_id | recipient_id | call_time           |
+-----------+--------------+---------------------+
| 8         | 4            | 2021-08-24 17:46:07 |
| 4         | 8            | 2021-08-24 19:57:13 |
| 5         | 1            | 2021-08-11 05:28:44 |
| 8         | 3            | 2021-08-17 04:04:15 |
| 11        | 3            | 2021-08-17 13:07:00 |
| 8         | 11           | 2021-08-17 22:22:22 |
+-----------+--------------+---------------------+

Result table:
+---------+
| user_id |
+---------+
| 1       |
| 4       |
| 5       |
| 8       |
+---------+

On 2021-08-24, the first and last call of this day for user 8 was with user 4. User 8 should be included in the answer.
Similary, user 4 on 2021-08-24 had their first and last call with user 8. User 4 should be included in the answer.
On 2021-08-11, user 1 and 5 had a call. This call was the only call for both of them on this day. Since this call is the first and last call of the day for both of them, they should both be included in the answer.
**/

WITH
    ranked_calls AS (
        SELECT
            user1, user2
            , ROW_NUMBER() OVER(PARTITION BY user1, call_date ORDER BY call_time) AS rnk1
            , ROW_NUMBER() OVER(PARTITION BY user1, call_date ORDER BY call_time DESC) AS rnk2
        FROM (
            SELECT 
                caller_id AS user1, recipient_id AS user2, call_time
                , SUBSTR(CAST(call_time AS STRING), 1, 10) AS call_date 
            FROM Calls
            UNION ALL
            SELECT
                recipient_id AS user1, caller_id AS user2, call_time
                , SUBSTR(CAST(call_time AS STRING), 1, 10) AS call_date 
            FROM Calls
        )
    )

SELECT
    a.user1
FROM (
    SELECT
        user1, user2
    FROM ranked_calls
    WHERE rnk1 = 1
) a
JOIN (
    SELECT
        user1, user2
    FROM ranked_calls
    WHERE rnk2 = 1
) b
ON
    a.user1 = b.user1
    AND a.call_date = b.call_date
GROUP BY
    a.user1
