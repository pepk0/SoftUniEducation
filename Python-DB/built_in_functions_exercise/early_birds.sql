SELECT
	user_id,
	starts_at - booked_at AS "Early Birds"
FROM
	bookings
WHERE
	starts_at - booked_at > INTERVAL '10 months'
