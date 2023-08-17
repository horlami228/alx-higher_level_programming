-- joining two tables

SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    WHERE state.id = cities.state_id;
