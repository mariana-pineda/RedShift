
CREATE TABLE youtube_metrics (
	category_id INTEGER, 
	channel_id VARCHAR(256), 
	channel_title VARCHAR(256), 
	comment_count INTEGER, 
	etag VARCHAR(256), 
	favourite_count INTEGER, 
	insert_dttm TIMESTAMPTZ, 
	kind VARCHAR(256), 
	like_count INTEGER, 
	live_actual_end_time TIMESTAMPTZ, 
	live_actual_start_time TIMESTAMPTZ, 
	live_scheduled_end_time TIMESTAMPTZ, 
	live_scheduled_start_time TIMESTAMPTZ, 
	published_date TIMESTAMPTZ, 
	thumbnail_url VARCHAR(256), 
	video_description VARCHAR(2000), 
	video_id VARCHAR(256), 
	video_title VARCHAR(256), 
	video_url VARCHAR(256), 
	view_count INTEGER, 
	category VARCHAR(256), 
	total_view_count INTEGER, 
	total_subscribers INTEGER, 
	total_video_count INTEGER
)

