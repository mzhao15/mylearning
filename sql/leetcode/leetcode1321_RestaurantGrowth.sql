WTIH
    daily_sum AS (
        SELECT
            visited_on, SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
    )

    , moving_window AS (
        SELECT
            a.visited_on,
            SUM(b.amount) AS amount,
            ROUND(AVG(b.amount), 2) average_amount
        FROM daily_sum a 
        JOIN daily_sum b
        ON b.visited_on BETWEEN a.visited_on 
            AND DATE_ADD(a.visited_on, INTERVAL 6 DAY)
        GROUP BY a.visited_on
        HAVING COUNT(1) = 7
    )

SELECT * FROM moving_window