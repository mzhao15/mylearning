WITH
    spending_desktop AS (
        SELECT
            *
        FROM Spending
        WHERE platform = 'desktop'
    )

    , spending_mobile AS (
        SELECT
            *
        FROM Spending
        WHERE platform = 'mobile'
    )

    , spendings AS (
        SELECT
            COALESCE(a.user_id, b.user_id) AS user_id,
            COALESCE(a.spend_date, a.spend_date) AS spend_date,
            -- a.platform AS platform_desktop,
            -- a.amount AS amount_desktop,
            -- b.platform AS platform_mobile,
            -- b.amount AS amount_mobile,
            COALESCE(a.amount, 0) + COALESCE(b.amount, 0) AS amount,
            CASE 
                WHEN a.platform IS NOT NULL and b.platform IS NULL THEN 'desktop'
                WHEN a.platform IS NOT and b.platform IS NOT NULL THEN 'mobile'
                ELSE 'both'
            END AS platform
        FROM spending_desktop a
        FULL OUTER JOIN spending_mobile b
        ON a.user_id = b.user_id AND a.spend_date = b.spend_date
    )

    , spendings_platform AS (
        SELECT
            spend_date, platform, 
            SUM(amount) AS total_amount,
            COUNT(DISTINCT user_id) AS total_users
        FROM spendings
        GROUP BY spend_date, platform
    )

    , platforms AS(
        SELECT 'mobile' AS platform
        UNION ALL
        SELECT 'desktop' AS platform
        UNION ALL
        SELECT 'both' AS platform
    )

    , categories AS (
        SELECT
            a.spend_date, b.platform
        FROM (SELECT DISTINCT spend_date FROM Spending) a, platforms b
    )

    , final AS (
        SELECT
            a.spend_date, a.platform,
            COALESCE(b.total_amount, 0) AS total_amount,
            COALESCE(b.total_users, 0) AS total_users
        FROM categories a 
        LEFT JOIN
            spendings_platform b
        ON
            a.spend_date = b.spend_date AND a.platform = b.platform
    )       


SELECT * FROM final
ORDER BY spend_date, platform