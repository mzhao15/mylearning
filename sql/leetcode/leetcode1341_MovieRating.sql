

/* 1 */

SELECT 
    a.name, COUNT(DISTINCT a.movie_id) AS no_of_rated_movies
FROM Movie_Rating a
JOIN Users b
ON a.user_id = b.user_id
GROUP BY b.name
ORDER BY no_of_rated_movies DESC, name
LIMIT 1





/* 2 */