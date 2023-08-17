-- create a table with fields with default and unique constraint

CREATE TABLE
    IF NOT EXISTS
    `unique_id`
    (id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
