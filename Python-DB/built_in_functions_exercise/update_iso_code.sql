UPDATE countries
SET iso_code = SUBSTRING(UPPER(country_name), 1, 3)
WHERE
	iso_code IS NULL
RETURNING *;
