-- Dimension Tables

CREATE TABLE dim_customer(
    customer_key INT PRIMARY KEY,
    customer_id VARCHAR(10),
    customer_name VARCHAR(20),
    customer_city VARCHAR(20)
);

CREATE TABLE dim_product(
    product_key INT PRIMARY KEY,
    product_id VARCHAR(10),
    product_name VARCHAR(20),
    category VARCHAR(20),
    price INT
);

CREATE TABLE dim_date(
    date_key INT PRIMARY KEY,
    order_date DATE,
    year INT,
    month INT,
    day INT
);

-- Fact Table
CREATE TABLE fact_sales(
    fact_sales_key INT PRIMARY KEY,
    date_key INT,
    customer_key INT,
    product_key INT,
    quantity INT,
    total_amount INT,

    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);

