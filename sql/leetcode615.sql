
WITH
    paytable AS (
        SELECT
            a.amount, month(a.pay_date) AS pay_month,
            b.department_id
        FROM salary a 
        JOIN employee b
        ON a.employee_id = b.employee_id
    )

    , avg_salary AS (
        SELECT
            DISTINCT
            pay_month, department_id,
            AVG(amount) OVER(PARTITION BY pay_month, department_id) AS department_avg,
            AVG(amount) OVER(PARTITION BY pay_month) AS company_avg
        FROM paytable
    )

SELECT 
    pay_month, department_id,
    CASE 
        WHEN department_avg > company_avg THEN 'higher'
        WHEN  department_avg < company_avg THEN 'lower'
    ELSE 'same' END AS comparison
FROM avg_salary
ORDER BY pay_month, department_id