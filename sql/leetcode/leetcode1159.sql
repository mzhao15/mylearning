
SELECT
    t.seller_id,
    CASE
        WHEN t.rnk = 2 AND t.item_brand = t.favorite_brand THEN 'Yes'
    ELSE 'No' END AS 2nd_item_fav_brand 
FROM (
    SELECT
        a.order_id,
        a.item_id,
        b.item_brand,
        c.user_id AS seller_id,
        c.favorite_brand,
        ROW_NUMBER() OVER(PARTITION BY c.user_id ORDER BY a.order_date) AS rnk,
        COUNT(order_id) OVER(PARTITION BY c.user_id) AS order_cnt
    FROM Orders a
    JOIN Items b
    ON a.item_id = b.item_id
    RIGHT JOIN Users c
    ON a.seller_id = c.user_id
) t
WHERE (t.order_cnt = 1 AND t.rnk = 1) OR (t.order_cnt > 1 AND t.rnk = 2)


SELECT
    a.seller_id
    , CASE WHEN i.item_brand = u.favorite_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand 
FROM Users u
LEFT JOIN (
    SELECT
        seller_id, item_id
    FROM (
        SELECT
            seller_id, item_id
            , ROW_NUMBER() OVER(PARTITION BY seller_id ORDER BY order_date) AS rnk
            --  can use RANK or DENSE_RANK too
            , COUNT() OVER(PARTITION BY seller_id) AS no_of_items
        FROM Orders
    ) t
    WHERE
        t.rnk = 2 or t.no_of_items < 2
) a
ON 
    a.seller_id = u.user_id 
JOIN Items i
ON
    a.item_id = i.item_id
