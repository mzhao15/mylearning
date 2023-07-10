/*
https://circlecoder.com/find-cumulative-salary-of-an-employee/

The Employee table holds the salary information in a year.

Write a SQL to get the cumulative sum of an employee’s salary over a period of 3 months but exclude the most recent month.

The result should be displayed by ‘Id’ ascending, and then by ‘Month’ descending.

Example Input

| Id | Month | Salary |
|----|-------|--------|
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |

Output
| Id | Month | Salary |
|----|-------|--------|
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
*/
SELECT
    t.Id, t.Month, t.Salary
FROM (
    SELECT
        Id, Month, e1.Salary + COALESCE(e2.Salary, 0) + COALESCE(e3.salary, 0) AS Salary
        , ROW_NUMBER() OVER(PARTITION BY Id ORDER BY Month DESC) rnk
    FROM Employee e1
    LEFT JOIN Employee e2
    ON
        e1.Id = e2.Id AND e1.Month = e2.Month + 1
    LEFT JOIN Employee e3
    ON
        e1.Id = e3.Id AND e1.Month = e3.Month + 2
) t
WHERE t.rnk != 1
ORDER BY t.Id, t.Month DESC
