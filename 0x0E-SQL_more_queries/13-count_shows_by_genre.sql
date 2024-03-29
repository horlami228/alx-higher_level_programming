-- list all tv genres
-- along with the count of shows with the genres
-- order in descending orders by number of shows linked

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
    FROM tv_genres
    INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    GROUP BY tv_genres.name
    ORDER BY number_of_shows DESC;
