
CREATE TABLE tpcds.promotion (
    p_promo_sk INT NOT NULL, 
    p_promo_id STRING NOT NULL, 
    p_start_date_sk INT, 
    p_end_date_sk INT, 
    p_item_sk INT, 
    p_cost DECIMAL(15, 2), 
    p_response_target INT, 
    p_promo_name STRING, 
    p_channel_dmail CHAR(1), 
    p_channel_email CHAR(1), 
    p_channel_catalog CHAR(1), 
    p_channel_tv CHAR(1), 
    p_channel_radio CHAR(1), 
    p_channel_press CHAR(1), 
    p_channel_event CHAR(1), 
    p_channel_demo CHAR(1), 
    p_channel_details STRING, 
    p_purpose CHAR(15), 
    p_discount_active CHAR(1), 
    PRIMARY KEY (p_promo_sk)
) USING DELTA
