-- leetcode 1327
-- List the Products in a Period

SELECT
    b.product_name, SUM(unit) AS unit
FROM Orders a
JOIN Products b
ON a.product_id = b.product_id
WHERE a.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY a.product_id
HAVING SUM(unit) >= 100