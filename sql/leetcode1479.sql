WITH
    items_category AS (
        SELECT
            dayofweek(a.order_date) AS dayinweek, a.quantity,
            b.item_category
        FROM Orders a
        RIGHT JOIN Items b
        ON a.item_id = b.item_id
    )

SELECT
    item_category AS category,
    SUM(CASE WHEN dayinweek = 1 THEN quantity ELSE 0 END) AS Sunday,
    SUM(CASE WHEN dayinweek = 2 THEN quantity ELSE 0 END) AS Monday,
    SUM(CASE WHEN dayinweek = 3 THEN quantity ELSE 0 END) AS Tuesday,
    SUM(CASE WHEN dayinweek = 4 THEN quantity ELSE 0 END) AS Wednesday,
    SUM(CASE WHEN dayinweek = 5 THEN quantity ELSE 0 END) AS Thursday,
    SUM(CASE WHEN dayinweek = 6 THEN quantity ELSE 0 END) AS Friday,
    SUM(CASE WHEN dayinweek = 7 THEN quantity ELSE 0 END) AS Saturday
FROM items_category
GROUP BY item_category

