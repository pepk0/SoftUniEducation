UPDATE projects
SET end_date = start_date + INTERVAL '5 Months'
WHERE 
	end_date IS NULL
RETURNING *;
