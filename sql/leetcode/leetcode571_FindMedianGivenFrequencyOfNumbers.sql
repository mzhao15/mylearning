/*
https://circlecoder.com/find-median-given-frequency-of-numbers/

The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

+--------+
| median |
+--------|
| 0.0000 |
+--------+
Write a query to find the median of all numbers and name the result as median.
*/


-- https://massivealgorithms.blogspot.com/2019/03/leetcode-571-find-median-given.html

WITH
    enhanced_numbers AS(
        SELECT
            Number, Frequency
            , SUM(Frequency) OVER(ORDER BY Number) AS current_count
            , SUM(Frequency) AS total_count
        FROM Numbers
    )

SELECT
    ROUND(SUM(Number) / COUNT(Number), 2) AS median
FROM enhanced_numbers
WHERE current_count BETWEEN total_count/2 AND total_count/2 + Frequency