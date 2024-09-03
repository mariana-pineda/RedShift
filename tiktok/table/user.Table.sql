
CREATE TABLE "user" (
	user_id INTEGER IDENTITY(1,1) NOT NULL, 
	first_name VARCHAR(256) NOT NULL, 
	last_name VARCHAR(256) NOT NULL, 
	display_name VARCHAR(256) NOT NULL, 
	email VARCHAR(256) NOT NULL, 
	role VARCHAR(256) NOT NULL, 
	status VARCHAR(256) NOT NULL, 
	CONSTRAINT user_pkey PRIMARY KEY (user_id)
)

