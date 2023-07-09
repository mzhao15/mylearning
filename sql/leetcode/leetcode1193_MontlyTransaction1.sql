
/* 1 */

SELECT
    DATE_FORMAT(trans_date, 'yyyy-MM') AS `month`, country,
    COUNT(id) AS trans_count,
    COUNT(CASE WHEN state = 'approved' THEN id ELSE NULL END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, 'yyyy-MM'), country



/* 2 */


WITH
    ta AS (
        SELECT
            a.*,
            b.trans_date AS chargeback_date
        FROM Transactions a
        LEFT JOIN Chargebacks b
        ON a.id = b.trans_id
    )

    , approved AS (
        SELECT
            DATE_FORMAT(trans_date, 'yyyy-MM') AS trans_month, country,
            COUNT(id) AS approved_count,
            SUM(amount) AS approved_amount
        FROM ta
        WHERE state = 'approved'
        GROUP BY DATE_FORMAT(trans_date, 'yyyy-MM'), country
    )

    , chargeback AS (
        SELECT
            DATE_FORMAT(chargeback_date, 'yyyy-MM') AS trans_month, country,
            COUNT(id) AS chargeback_count,
            SUM(amount) AS chargeback_amount
        FROM ta
        WHERE chargeback_date IS NOT NULL
        GROUP BY DATE_FORMAT(chargeback_date, 'yyyy-MM'), country
    )

    , final AS (
        SELECT
            COALESCE(a.trans_month, b.trans_month) AS `month`,
            COALESCE(a.country, b.country) AS country,
            a.approved_count,
            a.approved_amount,
            b.chargeback_count,
            b.chargeback_amount
        FROM approved a
        FULL OUTER JOIN chargeback
        ON a.trans_month = b.trans_month AND a.country = b.country
    )

SELECT * FROM final 
ORDER BY `month`, country