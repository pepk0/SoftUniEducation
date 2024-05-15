CREATE TABLE minions_birthdays(
	id serial NOT NULL UNIQUE,
	name VARCHAR(50),
	date_of_birth DATE DEFAULT NOW(),
	age int DEFAULT 0,
	present VARCHAR(100),
	party timestamptz
);
