
CREATE TABLE tpcds.time_dim (
    t_time_sk INTEGER NOT NULL, 
    t_time_id STRING NOT NULL, 
    t_time INTEGER, 
    t_hour INTEGER, 
    t_minute INTEGER, 
    t_second INTEGER, 
    t_am_pm STRING, 
    t_shift STRING, 
    t_sub_shift STRING, 
    t_meal_time STRING,
    PRIMARY KEY (t_time_sk)
) USING DELTA
