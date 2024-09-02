
CREATE TABLE tpcds.date_dim (
  d_date_sk INTEGER NOT NULL, 
  d_date_id STRING NOT NULL, 
  d_date DATE, 
  d_month_seq INTEGER, 
  d_week_seq INTEGER, 
  d_quarter_seq INTEGER, 
  d_year INTEGER, 
  d_dow INTEGER, 
  d_moy INTEGER, 
  d_dom INTEGER, 
  d_qoy INTEGER, 
  d_fy_year INTEGER, 
  d_fy_quarter_seq INTEGER, 
  d_fy_week_seq INTEGER, 
  d_day_name STRING, 
  d_quarter_name STRING, 
  d_holiday STRING, 
  d_weekend STRING, 
  d_following_holiday STRING, 
  d_first_dom INTEGER, 
  d_last_dom INTEGER, 
  d_same_day_ly INTEGER, 
  d_same_day_lq INTEGER, 
  d_current_day STRING, 
  d_current_week STRING, 
  d_current_month STRING, 
  d_current_quarter STRING, 
  d_current_year STRING
)
USING DELTA;

ALTER TABLE tpcds.date_dim ADD CONSTRAINT date_dim_pkey PRIMARY KEY (d_date_sk);
