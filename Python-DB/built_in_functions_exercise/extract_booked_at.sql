SELECT
	EXTRACT(year from booked_at) AS "YEAR",
	EXTRACT(month from booked_at) AS "MONTH",
	EXTRACT(day from booked_at) AS "DAY",
	EXTRACT(hour from booked_at) AS "HOUR",
	EXTRACT(minute from booked_at) AS "MINUTE",
	CEIL(EXTRACT(second from booked_at)) AS "SECOND"
FROM 
	bookings;
