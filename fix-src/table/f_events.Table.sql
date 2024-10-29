
CREATE TABLE purgo_playground.f_events (
	date VARCHAR(256), 
	event_name VARCHAR(256), 
	event_ts VARCHAR(256), 
	user_pseudo_id VARCHAR(256), 
	event_bundle_sequence_id BIGINT, 
	session_id BIGINT, 
	session_number BIGINT, 
	device_browser VARCHAR(256), 
	device_category VARCHAR(256), 
	city VARCHAR(256), 
	country VARCHAR(256), 
	region VARCHAR(256), 
	page_title VARCHAR(256), 
	adcontent VARCHAR(256), 
	campaign VARCHAR(256), 
	traffic_source VARCHAR(256), 
	traffic_medium VARCHAR(256), 
	referral_path VARCHAR(256), 
	keyword VARCHAR(256), 
	session_engaged VARCHAR(256), 
	content VARCHAR(256), 
	search_query VARCHAR(256), 
	form_name VARCHAR(256), 
	navigation_item_type VARCHAR(256), 
	navigation_item_name VARCHAR(256), 
	content_name VARCHAR(256), 
	engagement_time BIGINT
)
