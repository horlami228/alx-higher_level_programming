-- get the maximum value in a column with the MAX()
-- grouped by state
-- ordered by state

SELECT state, MAX(Value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
