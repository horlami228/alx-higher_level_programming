-- print avg(value) grouped by city in order of avg value descending
-- get between month of July and August
-- display only top 3 in descending order

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
