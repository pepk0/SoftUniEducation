CREATE TABLE employees(
	id serial PRIMARY KEY NOT NULL,
	first_name varchar(30),
	last_name varchar(50),
	hiring_date date DEFAULT '2023-01-01',
	salary numeric(10, 2),
	devices_number integer
);

CREATE TABLE departments(
	id serial PRIMARY KEY NOT NULL,
	name varchar(50),
	code char(3),
	description text
);

CREATE TABLE issues(
	id serial PRIMARY KEY NOT NULL,
	description varchar(150),
	date date,
	start timestamp
);
