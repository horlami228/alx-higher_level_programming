-- list all records by score and name in descending order of score
-- dont list rows where the name is empty

SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
