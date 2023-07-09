
-- Need to consider missing months. Use first_value and last_value

SELECT
    t1.requested_month AS `month`,
    SUM(t1.monthly_distance)/3 OVER(PARTITION BY t1.requested_quarter ORDER BY t1.requested_month) AS average_ride_distance,
    SUM(t1.monthly_duration)/3 OVER(PARTITION BY t1.requested_quarter ORDER BY t1.requested_month) AS average_ride_duration
FROM (
    SELECT
        t.requested_quarter, t.requested_month, 
        SUM(a.ride_distance) AS monthly_distance,
        SUM(a.ride_duration) AS monthly_duration
    FROM (
        SELECT
            a.ride_id, a.ride_distance, a.ride_duration, 
            b.requested_at, 
            month(b.requested_at) AS requested_month,
            quarter(b.requested_at) AS requested_quarter
        FROM AcceptedRides a
        JOIN Rides b
        ON a.ride_id = b.ride_id
        WHERE b.requested_at BETWEEN '2020-01-01' AND '2020-12-31'
    ) t
    GROUP BY t.requested_quarter, t.requested_month
) t1

