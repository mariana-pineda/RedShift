
CREATE TABLE tpcds.store (
	s_store_sk INTEGER NOT NULL, 
	s_store_id CHAR(16) NOT NULL, 
	s_rec_start_date DATE, 
	s_rec_end_date DATE, 
	s_closed_date_sk INTEGER, 
	s_store_name VARCHAR(50), 
	s_number_employees INTEGER, 
	s_floor_space INTEGER, 
	s_hours CHAR(20), 
	s_manager VARCHAR(40), 
	s_market_id INTEGER, 
	s_geography_class VARCHAR(100), 
	s_market_desc VARCHAR(100), 
	s_market_manager VARCHAR(40), 
	s_division_id INTEGER, 
	s_division_name VARCHAR(50), 
	s_company_id INTEGER, 
	s_company_name VARCHAR(50), 
	s_street_number VARCHAR(10), 
	s_street_name VARCHAR(60), 
	s_street_type CHAR(15), 
	s_suite_number CHAR(10), 
	s_city VARCHAR(60), 
	s_county VARCHAR(30), 
	s_state CHAR(2), 
	s_zip CHAR(10), 
	s_country VARCHAR(20), 
	s_gmt_offset NUMERIC(5, 2), 
	s_tax_precentage NUMERIC(5, 2), 
	CONSTRAINT store_pkey PRIMARY KEY (s_store_sk)
) DISTSTYLE ALL

