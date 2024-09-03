
CREATE TABLE users (
	user_id INTEGER IDENTITY(1,1) NOT NULL, 
	first_name VARCHAR(256) NOT NULL, 
	last_name VARCHAR(256) NOT NULL, 
	display_name VARCHAR(256) NOT NULL, 
	email VARCHAR(256) NOT NULL, 
	role_id INTEGER, 
	status VARCHAR(256), 
	CONSTRAINT users_pkey PRIMARY KEY (user_id)
)

