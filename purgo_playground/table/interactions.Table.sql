
CREATE TABLE purgo_playground.interactions (
  interaction_id INT NOT NULL, 
  enrollment_id INT NOT NULL, 
  interaction_date TIMESTAMP
);

ALTER TABLE purgo_playground.interactions ADD CONSTRAINT primary_key_interactions PRIMARY KEY (interaction_id);
