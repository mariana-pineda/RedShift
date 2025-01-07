
CREATE TABLE purgo_playground.interactions (
  interaction_id INT NOT NULL,
  enrollment_id INT NOT NULL,
  interaction_date TIMESTAMP
)
COMMENT "Table to store interaction details with enrollment and timestamp information, adjusted for Databricks";
