
CREATE TABLE purgo_playground.interactions (
  interaction_id INT NOT NULL, 
  enrollment_id INT NOT NULL, 
  interaction_date TIMESTAMP
);

ALTER TABLE purgo_playground.interactions
ADD PRIMARY KEY (interaction_id, enrollment_id);
