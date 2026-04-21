-- Truncates existing data, loads fresh data from S3 stages into ORDERS_DETAILED and CUSTOMER_SUMMARY tables, and retrieves records for validation.

-- ORDERS_DETAILED
TRUNCATE TABLE ORDERS_DETAILED;
COPY INTO ORDERS_DETAILED FROM @ORDERS_DETAILED_STAGE;

-- CUSTOMER_SUMMARY
TRUNCATE TABLE CUSTOMER_SUMMARY;
COPY INTO CUSTOMER_SUMMARY FROM @CUSTOMER_SUMMARY_STAGE;


-- Retrieve all records from the ORDERS_DETAILED table
SELECT * FROM ORDERS_DETAILED;

-- Retrieve all records from the CUSTOMER_SUMMARY table
SELECT * FROM CUSTOMER_SUMMARY;


-- Classifies customers into segments based on their state (region) by assigning High, Medium, or Low value categories for analysis.
SELECT
    customer_id,
    customer_city,
    customer_state,
    total_orders,
    CASE
        WHEN customer_state IN ('SP', 'RJ') THEN 'High Value Region'
        WHEN customer_state IN ('MG', 'RS') THEN 'Medium Value Region'
        ELSE 'Low Value Region'
    END AS customer_segment
FROM customer_summary;
    

