
CREATE TABLE purgo_playground.interactions (
  interaction_id INT,
  enrollment_id INT,
  interaction_date TIMESTAMP
)
USING DELTA;
