WITH
    temp (
        SELECT
            employee_id, name, salary
            , COUNT(employee_id) OVER(PARTITION BY salary) AS cnt
        FROM Employees
    )
    
    , temp1 AS (
        SELECT
            employee_id, name, salary
            , DENSE_RANK() OVER(ORDER BY salary) AS team_id
        FROM temp 
        WHERE cnt > 1
    )
SELECT * FROM temp1
ORDER BY team_id, employee_id