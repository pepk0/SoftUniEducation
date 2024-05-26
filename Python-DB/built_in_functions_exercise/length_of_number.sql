SELECT
	population,
	CHAR_LENGTH(population::varchar) AS "length"
FROM
	countries;