
CREATE TABLE tpcds.call_center (
	cc_call_center_sk INTEGER NOT NULL, 
	cc_call_center_id STRING NOT NULL, 
	cc_rec_start_date DATE, 
	cc_rec_end_date DATE, 
	cc_closed_date_sk INTEGER, 
	cc_open_date_sk INTEGER, 
	cc_name STRING, 
	cc_class STRING, 
	cc_employees INTEGER, 
	cc_sq_ft INTEGER, 
	cc_hours STRING, 
	cc_manager STRING, 
	cc_mkt_id INTEGER, 
	cc_mkt_class STRING, 
	cc_mkt_desc STRING, 
	cc_market_manager STRING, 
	cc_division INTEGER, 
	cc_division_name STRING, 
	cc_company INTEGER, 
	cc_company_name STRING, 
	cc_street_number STRING, 
	cc_street_name STRING, 
	cc_street_type STRING, 
	cc_suite_number STRING, 
	cc_city STRING, 
	cc_county STRING, 
	cc_state STRING, 
	cc_zip STRING, 
	cc_country STRING, 
	cc_gmt_offset DECIMAL(5, 2), 
	cc_tax_percentage DECIMAL(5, 2), 
	PRIMARY KEY (cc_call_center_sk)
) USING DELTA
