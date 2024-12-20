
CREATE TABLE purgo_playground.enrollments (
  enrollment_id INT NOT NULL COMMENT 'This is the primary identifier for enrollments', 
  program_id INT NOT NULL COMMENT 'This is the identifier for programs', 
  enrollment_date TIMESTAMP COMMENT 'This is the date of enrollment'
)
USING DELTA;
