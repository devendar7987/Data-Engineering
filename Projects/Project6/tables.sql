-- Create or replace the ORDERS_DETAILED table to store order-level and customer-level details
CREATE OR REPLACE TABLE ORDERS_DETAILED(
    customer_id STRING,
    order_id STRING,
    order_status STRING,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,
    customer_unique_id STRING,
    customer_zip_code_prefix INT,
    customer_city STRING,
    customer_state STRING,
    order_category STRING,
    customer_key STRING
);


-- Create or replace the CUSTOMER_SUMMARY table to store aggregated customer order information
CREATE OR REPLACE TABLE CUSTOMER_SUMMARY(
    customer_id STRING,
    customer_city STRING,
    customer_state STRING,
    total_orders INT
);