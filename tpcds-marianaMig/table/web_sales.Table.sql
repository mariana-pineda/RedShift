
CREATE TABLE tpcds.web_sales (
    ws_sold_date_sk INTEGER, 
    ws_sold_time_sk INTEGER, 
    ws_ship_date_sk INTEGER, 
    ws_item_sk INTEGER NOT NULL, 
    ws_bill_customer_sk INTEGER, 
    ws_bill_cdemo_sk INTEGER, 
    ws_bill_hdemo_sk INTEGER, 
    ws_bill_addr_sk INTEGER, 
    ws_ship_customer_sk INTEGER, 
    ws_ship_cdemo_sk INTEGER, 
    ws_ship_hdemo_sk INTEGER, 
    ws_ship_addr_sk INTEGER, 
    ws_web_page_sk INTEGER, 
    ws_web_site_sk INTEGER, 
    ws_ship_mode_sk INTEGER, 
    ws_warehouse_sk INTEGER, 
    ws_promo_sk INTEGER, 
    ws_order_number BIGINT NOT NULL, 
    ws_quantity INTEGER, 
    ws_wholesale_cost DECIMAL(7, 2), 
    ws_list_price DECIMAL(7, 2), 
    ws_sales_price DECIMAL(7, 2), 
    ws_ext_discount_amt DECIMAL(7, 2), 
    ws_ext_sales_price DECIMAL(7, 2), 
    ws_ext_wholesale_cost DECIMAL(7, 2), 
    ws_ext_list_price DECIMAL(7, 2), 
    ws_ext_tax DECIMAL(7, 2), 
    ws_coupon_amt DECIMAL(7, 2), 
    ws_ext_ship_cost DECIMAL(7, 2), 
    ws_net_paid DECIMAL(7, 2), 
    ws_net_paid_inc_tax DECIMAL(7, 2), 
    ws_net_paid_inc_ship DECIMAL(7, 2), 
    ws_net_paid_inc_ship_tax DECIMAL(7, 2), 
    ws_net_profit DECIMAL(7, 2)
);

ALTER TABLE tpcds.web_sales ADD CONSTRAINT web_sales_pkey PRIMARY KEY (ws_item_sk, ws_order_number);
