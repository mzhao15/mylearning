

WTIH 
    tasks AS (
        SELECT
            DISTINCT
            task_id,
            1 AS subtask_id
        FROM Tasks
    )

    , subtasks AS (
        SELECT 
            task_id, subtask_id
        FROM tasks

        UNION ALL

        SELECT
            a.task_id, a.subtask_id + 1 AS subtask_id 
        FROM (
            SELECT
                task_id, MAX(subtask_id) AS subtask_id
            FROM subtasks
            GROUP BY task_id
        ) a, Tasks b
        ON a.task_id = b.task_id
        WHERE a.subtask_id < b.subtasks_count
    )

    , missing_subtasks AS (
        SELECT
            a.*
        FROM subtaks a
        LEFT JOIN executed b
        ON a.task_id = b.task_id AND a.subtask_id = b.subtask_id
        WHERE b.task_id IS NULL
    )
SELECT * FROM missing_subtasks