WITH
    temp AS (
        SELECT
            order_id
            , MAX(quantity) AS max_quantity
            , SUM(quantity)/COUNT(order_id) AS avg_quanty
        FROM OrdersDetails
        GROUP BY order_id
    )

SELECT
    order_id
FROM temp 
WHERE
    max_quantity > (SELECT MAX(avg_quanty) FROM temp)
ORDER BY order_id
