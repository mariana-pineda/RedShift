CREATE SCHEMA IF NOT EXISTS purgo_playground;

DROP TABLE IF EXISTS purgo_playground.programs;
DROP TABLE IF EXISTS purgo_playground.interactions;
DROP TABLE IF EXISTS purgo_playground.f_order;
DROP TABLE IF EXISTS purgo_playground.f_item;
DROP TABLE IF EXISTS purgo_playground.f_inv_movmnt;
DROP TABLE IF EXISTS purgo_playground.f_events;
DROP TABLE IF EXISTS purgo_playground.enrollments;
DROP TABLE IF EXISTS purgo_playground.d_product;
DROP TABLE IF EXISTS purgo_playground.countries;
DROP TABLE IF EXISTS purgo_playground.f_sales;
DROP TABLE IF EXISTS purgo_playground.psek;
DROP TABLE IF EXISTS purgo_playground.pchk;
DROP TABLE IF EXISTS purgo_playground.parl;
DROP TABLE IF EXISTS purgo_playground.pbev;
DROP TABLE IF EXISTS purgo_playground.l009t;
DROP TABLE IF EXISTS purgo_playground.vbax;
DROP TABLE IF EXISTS purgo_playground.para;

CREATE TABLE IF NOT EXISTS purgo_playground.programs (
  program_id BIGINT NOT NULL,
  program_name STRING NOT NULL,
  country_code STRING NOT NULL,
  program_start_date TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.interactions (
  interaction_id BIGINT NOT NULL,
  enrollment_id BIGINT NOT NULL,
  interaction_date TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.f_order (
  order_nbr STRING,
  order_type BIGINT,
  delivery_dt DECIMAL(38, 0),
  order_qty DOUBLE,
  sched_dt DECIMAL(38, 0),
  expected_shipped_dt DECIMAL(38, 0),
  actual_shipped_dt DECIMAL(38, 0),
  order_line_nbr STRING,
  loc_tracker_id STRING,
  shipping_add STRING,
  primary_qty DOUBLE,
  open_qty DOUBLE,
  shipped_qty DOUBLE,
  order_desc STRING,
  flag_return STRING,
  flag_cancel STRING,
  cancel_dt DECIMAL(38, 0),
  cancel_qty DOUBLE,
  crt_dt TIMESTAMP,
  updt_dt TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.f_item (
  item_nbr STRING,
  item_vb BIGINT,
  delivery_dt DECIMAL(38, 0),
  item_inv_type STRING,
  txn_nbr STRING,
  primary_qty DOUBLE,
  qty_in_hand DOUBLE,
  qty_on_hold DOUBLE,
  item_serial_nbr STRING,
  package_nbr STRING,
  crt_dt TIMESTAMP,
  updt_dt TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.f_inv_movmnt (
  txn_id STRING,
  inv_loc STRING,
  financial_qty DOUBLE,
  net_qty DOUBLE,
  expired_qt DECIMAL(38, 0),
  item_nbr STRING,
  unit_cost DOUBLE,
  um_rate DOUBLE,
  plant_loc_cd STRING,
  inv_stock_reference STRING,
  stock_type STRING,
  qty_on_hand DOUBLE,
  qty_shipped DOUBLE,
  cancel_dt DECIMAL(38, 0),
  flag_active STRING,
  crt_dt TIMESTAMP,
  updt_dt TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.f_events (
  date STRING,
  event_name STRING,
  event_ts STRING,
  user_pseudo_id STRING,
  event_bundle_sequence_id BIGINT,
  session_id BIGINT,
  session_number BIGINT,
  device_browser STRING,
  device_category STRING,
  city STRING,
  country STRING,
  region STRING,
  page_title STRING,
  adcontent STRING,
  campaign STRING,
  traffic_source STRING,
  traffic_medium STRING,
  referral_path STRING,
  keyword STRING,
  session_engaged STRING,
  content STRING,
  search_query STRING,
  form_name STRING,
  navigation_item_type STRING,
  navigation_item_name STRING,
  content_name STRING,
  engagement_time BIGINT
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.enrollments (
  enrollment_id BIGINT NOT NULL,
  program_id BIGINT NOT NULL,
  enrollment_date TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.d_product (
  prod_id STRING,
  item_nbr STRING,
  unit_cost DOUBLE,
  prod_exp_dt DECIMAL(38, 0),
  cost_per_pkg DOUBLE,
  plant_add STRING,
  plant_loc_cd STRING,
  prod_line STRING,
  stock_type STRING,
  pre_prod_days DOUBLE,
  sellable_qty DOUBLE,
  prod_ordr_tracker_nbr STRING,
  max_order_qty STRING,
  flag_active STRING,
  crt_dt TIMESTAMP,
  updt_dt TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.countries (
  country_code STRING,
  country_name STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.f_sales (
  sale_id BIGINT,
  product_id STRING,
  sale_date TIMESTAMP,
  sale_amount DOUBLE
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.psek (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.pchk (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.parl (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.pbev (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.l009t (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.vbax (
  id STRING,
  description STRING
) USING DELTA;

CREATE TABLE IF NOT EXISTS purgo_playground.para (
  id STRING,
  description STRING
) USING DELTA;
