/*
https://circlecoder.com/median-employee-salary/

The Employee table holds all employees. The employee table has three columns: Employee Id, Company Name, and Salary.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+
Write a SQL query to find the median salary of each company. Bonus points if you can solve it without using any built-in SQL functions.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+
*/

WITH
    stats AS (
        SELECT
            Id, Company, Salary
            , COUNT() OVER(PARTITION BY Company) AS employee_count
            , RANK() OVER(PARTITION BY Compnay ORDER BY Salary) AS salary_rank
        FROM Employee
    )
    , median_rank AS (
        SELECT Id, Company, Salary, salary_rank, CEIL(employee_count/2) AS median_rank FROM stats
        UNION
        SELECT 
            Id, Company, Salary, salary_rank
            , CASE 
                WHEN employee_count % 2 = 0 THEN CEIL(employee_count)/2+1
                ELSE CEIL(employee_count/2)
            END AS median_rank
        FROM stats
    )
SELECT
    Id, Company, Salary
FROM median_rank
WHERE median_rank = salary_rank
ORDER BY Company, Salary



SELECT
    Id, Company, Salary
FROM (
    SELECTs
        Id, Company, Salary
        , COUNT() OVER(PARTITION BY Company) AS employee_count
        , RANK() OVER(PARTITION BY Compnay ORDER BY Salary) AS salary_rank
    FROM Employee
) t
WHERE t.salary_rank BETWEEN employee_count/2 AND employee_count/2 + 1
