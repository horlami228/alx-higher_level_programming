-- get all tv shows and all genres linked to the shows
--  order by show title and genre name in ascending order
-- display NULL if a show does not have a genre

SELECT tv_shows.title, tv_genres.name
    FROM tv_shows
    LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id

    LEFT JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY tv_shows.title, tv_genres.name;
