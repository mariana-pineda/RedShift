
CREATE TABLE purgo_playground.interactions (
	interaction_id INT NOT NULL, 
	enrollment_id INT NOT NULL, 
	interaction_date TIMESTAMP
);

-- Databricks SQL does not support SQL Server syntax for specifying primary keys during table creation,
-- so ensure primary key constraints are managed within the application or logical model.
