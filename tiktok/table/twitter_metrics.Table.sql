
CREATE TABLE twitter_metrics (
	created_at TIMESTAMPTZ, 
	edit_history_tweet_ids VARCHAR(256), 
	followers INTEGER, 
	following INTEGER, 
	hashtags VARCHAR(1000), 
	impression_count INTEGER, 
	insert_dttm TIMESTAMPTZ, 
	like_count INTEGER, 
	media_key VARCHAR(256), 
	media_type VARCHAR(256), 
	media_url VARCHAR(256), 
	quote_count INTEGER, 
	reply_count INTEGER, 
	retweet_count INTEGER, 
	text VARCHAR(2000), 
	tweet_id VARCHAR(256), 
	tweet_url VARCHAR(256), 
	video_view_count INTEGER
)

