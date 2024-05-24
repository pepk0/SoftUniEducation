SELECT
	last_name,
	COUNT(notes) AS notes_with_dumbledore
FROM 
	wizard_deposits
WHERE
	notes LIKE '%Dumbledor%'
GROUP BY
	last_name;
