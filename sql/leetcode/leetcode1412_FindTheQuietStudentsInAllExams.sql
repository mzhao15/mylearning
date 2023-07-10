/*
https://circlecoder.com/find-the-quiet-students-in-all-exams/

Table: Student

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| student_id          | int     |
| student_name        | varchar |
+---------------------+---------+
student_id is the primary key for this table.
student_name is the name of the student.
Table: Exam

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| exam_id       | int     |
| student_id    | int     |
| score         | int     |
+---------------+---------+
(exam_id, student_id) is the primary key for this table.
Student with student_id got score points in exam with id exam_id.
A “quite” student is the one who took at least one exam and didn’t score neither the high score nor the low score.

Write an SQL query to report the students (student_id, student_name) being “quiet” in ALL exams.

Don’t return the student who has never taken any exam. Return the result table ordered by student_id.

The query result format is in the following example.

Student table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
| 3           | Stella        |
| 4           | Jonathan      |
| 5           | Will          |
+-------------+---------------+

Exam table:
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
| 20         |     1        |    80     |
| 30         |     1        |    70     |
| 30         |     3        |    80     |
| 30         |     4        |    90     |
| 40         |     1        |    60     |
| 40         |     2        |    70     |
| 40         |     4        |    80     |
+------------+--------------+-----------+

Result table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+

For exam 1: Student 1 and 3 hold the lowest and high score respectively.
For exam 2: Student 1 hold both highest and lowest score.
For exam 3 and 4: Studnet 1 and 4 hold the lowest and high score respectively.
Student 2 and 5 have never got the highest or lowest in any of the exam.
Since student 5 is not taking any exam, he is excluded from the result.
So, we only return the information of Student 2.
*/
SELECT
    t.student_id, t.student_name
FROM (
    SELECT
        e.student_id, e.student_name, e.exam_id
        , COUNT(e.exam_id) OVER(PARTITION BY e.student_id) AS no_of_exams_taken
        , MAX(e.score) OVER(PARTITION BY e.exam_id ORDER BY e.score DESC) AS max_score
        , MIN(e.score) OVER(PARTITION BY e.exam_id ORDER BY e.score) AS min_score
        , COUNT(e.exam_id) AS total_exams
    FROM Exam e
    JOIN Student s
    ON e.student_id = s.student_id
) t
WHERE t.no_of_exams_taken > 1
    AND t.score != t.max_score
    AND t.score != t.min_score
GROUP BY t.student_id, t.student_name
HAVING COUNT(t.exam_id) = t.total_exams
ORDER BY t.student_id


WITH
    c AS (
        SELECT
            t.student_id
        FROM (
            SELECT
                student_id, exam_id, score
                , COUNT(e.exam_id) OVER(PARTITION BY e.student_id) AS no_of_exams_taken
                , MAX(e.score) OVER(PARTITION BY e.exam_id ORDER BY e.score DESC) AS max_score
                , MIN(e.score) OVER(PARTITION BY e.exam_id ORDER BY e.score) AS min_score
            FROM Exams   
        ) t
        WHERE t.no_of_exams_taken = 1
            OR t.score = max_score OR t.score = min_score
        GROUP BY t.student_id
    )
    , students_took_exams AS (
        SELECT
            student_id
        FROM Exam
        GROUP BY student_id
    )
SELECT
    a.student_id, a.student_name
FROM students_took_exams a
JOIN Student b
ON a.student_id = b.student_id
LEFT JOIN students_took_exams c
ON a.student_id = c.student_id
WHERE c.student_id IS NULL
ORDER BY a.student_id

