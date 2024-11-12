
CREATE TABLE purgo_playground.interactions (
  interaction_id INT NOT NULL, 
  enrollment_id INT NOT NULL, 
  interaction_date TIMESTAMP
)
USING DELTA
OPTIONS (
  primaryKey = 'interaction_id'
);
