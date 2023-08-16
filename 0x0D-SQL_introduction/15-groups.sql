-- list number of records with the same score
-- result column should be number
-- group by score and number in descending order

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;