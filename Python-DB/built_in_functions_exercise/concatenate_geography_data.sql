CREATE VIEW view_continents_countries_currencies_details AS
	SELECT 
		CONCAT(
			con.continent_name,
			': ',
			con.continent_code
		) AS continent_details,
		CONCAT_WS(
			' - ',
			co.country_name,
			co.capital,
			co.area_in_sq_km,
			'km2'
		) AS country_information,
		CONCAT(
			cu.description,
			' ',
			'(',
			cu.currency_code,
			')'
		) AS currencies
	FROM 
		countries AS co, continents AS con, currencies AS cu
	WHERE
		co.continent_code = con.continent_code AND co.currency_code = cu.currency_code
	ORDER BY
		country_information, currencies;
	