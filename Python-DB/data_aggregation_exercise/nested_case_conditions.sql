CREATE VIEW view_performance_rating AS
	SELECT
		first_name,
		last_name,
		job_title,
		salary,
		department_id,
		CASE
			WHEN salary >= 25000 THEN -- if condition:
			CASE -- inner if condition the above condition will return the inners return
				WHEN job_title LIKE 'Senior%' THEN 'High-performing Senior'
				ELSE 'High-performing Employee'
			END
			ELSE 'Average-performing'
		END AS performance_rating
	FROM
		employees;
