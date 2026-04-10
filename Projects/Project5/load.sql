-- Full Load (Batch Load)

-- Customers
TRUNCATE TABLE customers;
COPY INTO customers FROM @customers_stage;

-- Orders
TRUNCATE TABLE orders;
COPY INTO orders FROM @orders_stage;

-- Payments
TRUNCATE TABLE payments;
COPY INTO payments FROM @payments_stage;


-- Verify total number of records loaded into each table after full load

SELECT COUNT(*) AS customer_count FROM customers;
SELECT COUNT(*) AS order_count FROM orders;
SELECT COUNT(*) AS payment_count FROM payments;


-- Calculate total runtime (in seconds) of all COPY INTO operations executed in the last 5 minutes

SELECT
    SUM(TOTAL_ELAPSED_TIME)/1000 AS total_load_time_seconds
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE QUERY_TEXT ILIKE 'COPY INTO%'
AND START_TIME >= DATEADD(MINUTE, -5, CURRENT_TIMESTAMP());






