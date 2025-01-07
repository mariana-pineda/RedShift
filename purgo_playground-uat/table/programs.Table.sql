
CREATE TABLE purgo_playground.programs (
    program_id INT NOT NULL COMMENT 'Primary key: Consider adding a COMMENT to indicate primary key manually as Databricks does not support primary key constraints.',
    program_name STRING NOT NULL,
    country_code STRING NOT NULL,
    program_start_date TIMESTAMP
) USING DELTA

