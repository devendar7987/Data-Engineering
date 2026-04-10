-- Create or replace a table named customers
CREATE OR REPLACE TABLE customers(
    customer_id INT,
    name STRING,
    city STRING
);

-- Create or replace a table named orders
CREATE OR REPLACE TABLE orders(
    order_id INT,
    customer_id INT,
    amount INT
);

-- Create or replace a table named payments
CREATE OR REPLACE TABLE payments(
    payment_id INT,
    order_id INT,
    status STRING
);