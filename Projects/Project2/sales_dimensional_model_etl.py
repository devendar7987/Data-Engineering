# Loading Single Table Data into Dimensions and Fact Table (Star Schema)

import pandas as pd
from sqlalchemy import create_engine

def extract(file_name):
    print(f"Extracting data from {file_name}")
    return pd.read_csv(file_name)

def transform(data_frame):
    print("Transforming data...")
    df_clean = data_frame.copy()

    # Date conversion
    df_clean["order_date"] = pd.to_datetime(data_frame["order_date"])

    # Remove invalid records
    df_clean = df_clean.dropna(subset = ['customer_id', 'product_id', 'order_date','quantity', 'price'])

    # Standardize text columns
    df_clean['customer_name'] = df_clean['customer_name'].str.strip().str.title()
    df_clean['customer_city'] = df_clean['customer_city'].str.strip().str.title()
    df_clean['product_name'] = df_clean['product_name'].str.strip().str.title()
    df_clean['category'] = df_clean['category'].str.strip().str.upper()

    # Ensure numeric types
    df_clean['quantity'] = df_clean['quantity'].astype(int)
    df_clean['price'] = df_clean['price'].astype(int)

    return df_clean

def load(data_frame, table_name, engine):
    print(f"Loading data into {table_name} table...")
    data_frame.to_sql(table_name, engine, if_exists="append", index=False)


# Extract data from the source file
extracted_data = extract("sales_raw.csv")
print("Extracted data from source file:")
print(extracted_data)

# Transform the extracted data
transformed_data = transform(extracted_data)
print("Transformed data")
print(transformed_data)


# Create Dimension Tables

# Customer Dimension
dim_customer = transformed_data[['customer_id', 'customer_name', 'customer_city']].drop_duplicates().reset_index(drop = True)
dim_customer['customer_key'] = dim_customer.index + 1
print("Dimension: dim_customer")
print(dim_customer)

# Product Dimension
dim_product = transformed_data[['product_id', 'product_name', 'category', 'price']].drop_duplicates().reset_index(drop = True)
dim_product['product_key'] = dim_product.index + 1
print("Dimension: dim_product")
print(dim_product)

# Date Dimension
dim_date = transformed_data[['order_date']].drop_duplicates().reset_index(drop = True)
dim_date['date_key'] = dim_date['order_date'].dt.strftime('%Y%m%d').astype(int)
dim_date['year'] = dim_date['order_date'].dt.year
dim_date['month'] = dim_date['order_date'].dt.month
dim_date['day'] = dim_date['order_date'].dt.day
print("Dimension: dim_date")
print(dim_date)

# Create Staging Fact
fact_stage = transformed_data.merge(dim_customer, on=['customer_id','customer_name','customer_city'])\
.merge(dim_product, on=['product_id','product_name','category','price'])\
.merge(dim_date, on=['order_date'])
fact_stage['total_amount'] = fact_stage['quantity'] * fact_stage['price']
print("Fact: fact_stage")
print(fact_stage)

# Create Final Fact Table
fact_sales = fact_stage[['date_key', 'customer_key', 'product_key', 'quantity', 'total_amount']].copy()
fact_sales['fact_sales_key'] = fact_sales.index + 1
print("Fact: fact_sales")
print(fact_sales)

# Load the Dimension Tables and Fact Table into the database

username = "postgres"
password = "chintu7987" 
host = "localhost"
port = 5432
database_name = "Datacamp"

db_engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}"
)

load(dim_customer, "dim_customer", db_engine)
load(dim_product, "dim_product", db_engine)
load(dim_date, "dim_date", db_engine)
load(fact_sales, "fact_sales", db_engine)

# Validate loaded data
dim_customer_check = pd.read_sql("SELECT * FROM dim_customer;", db_engine)
print("Validating dim_customer table...")
print(dim_customer_check)

dim_product_check = pd.read_sql("SELECT * FROM dim_product;", db_engine)
print("Validating dim_product table...")
print(dim_product_check)

dim_date_check = pd.read_sql("SELECT * FROM dim_date;", db_engine)
print("Validating dim_date table...")
print(dim_date_check)

fact_sales_check = pd.read_sql("SELECT * FROM fact_sales;", db_engine)
print("Validating fact_sales table...")
print(fact_sales_check)

# Check whether foreign key relationships are established
# between the fact_sales table (child) and its parent dimension tables
query = """
SELECT
    conname,
    conrelid::regclass AS child_table,
    confrelid::regclass AS parent_table
FROM pg_constraint
WHERE contype = 'f'
  AND conrelid = 'fact_sales'::regclass;
"""
fact_sales_fk_check = pd.read_sql(query, db_engine)
print("Validating foreign key relationships for fact_sales table...")

print(fact_sales_fk_check)
