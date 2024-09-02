
CREATE TABLE tpcds.web_site (
	web_site_sk INTEGER NOT NULL, 
	web_site_id CHAR(16) NOT NULL, 
	web_rec_start_date DATE, 
	web_rec_end_date DATE, 
	web_name VARCHAR(50), 
	web_open_date_sk INTEGER, 
	web_close_date_sk INTEGER, 
	web_class VARCHAR(50), 
	web_manager VARCHAR(40), 
	web_mkt_id INTEGER, 
	web_mkt_class VARCHAR(50), 
	web_mkt_desc VARCHAR(100), 
	web_market_manager VARCHAR(40), 
	web_company_id INTEGER, 
	web_company_name CHAR(50), 
	web_street_number CHAR(10), 
	web_street_name VARCHAR(60), 
	web_street_type CHAR(15), 
	web_suite_number CHAR(10), 
	web_city VARCHAR(60), 
	web_county VARCHAR(30), 
	web_state CHAR(2), 
	web_zip CHAR(10), 
	web_country VARCHAR(20), 
	web_gmt_offset NUMERIC(5, 2), 
	web_tax_percentage NUMERIC(5, 2), 
	CONSTRAINT web_site_pkey PRIMARY KEY (web_site_sk)
) DISTSTYLE ALL

