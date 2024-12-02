
CREATE TABLE purgo_playground.programs (
    program_id INT,
    program_name STRING,
    country_code STRING,
    program_start_date TIMESTAMP
)
USING DELTA;

ALTER TABLE purgo_playground.programs ADD CONSTRAINT pk_program_id PRIMARY KEY (program_id);
