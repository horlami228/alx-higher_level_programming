-- print avg(value) grouped by city in order of avg value descending

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
