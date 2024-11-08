
CREATE TABLE purgo_playground.programs (
    program_id INT NOT NULL, 
    program_name STRING NOT NULL, 
    country_code STRING NOT NULL, 
    program_start_date TIMESTAMP
);

ALTER TABLE purgo_playground.programs ADD CONSTRAINT programs_pk PRIMARY KEY (program_id);
