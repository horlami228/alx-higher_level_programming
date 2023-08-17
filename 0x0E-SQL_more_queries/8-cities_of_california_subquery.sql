-- list all the cities of California in the database

SELECT id, name
    FROM cities
    WHERE states.id = 1
    ORDER BY id ASC;
