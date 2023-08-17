-- list all the cities of California in the database

SELECT id, name
    FROM cities
    WHERE states.name = "California"
    ORDER BY id ASC;
