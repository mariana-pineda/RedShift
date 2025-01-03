
CREATE TABLE purgo_playground.enrollments (
    enrollment_id INT, 
    program_id INT, 
    enrollment_date TIMESTAMP
);

ALTER TABLE purgo_playground.enrollments ADD CONSTRAINT enrollment_id_pk PRIMARY KEY (enrollment_id);
