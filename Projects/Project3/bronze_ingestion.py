# Databricks notebook source
# Bronze Layer - Raw Data Ingestion

print("Starting Bronze Layer - Raw Ingestion Process...")

# Reading source tables
print("Reading source tables...")

customers_df = spark.table("customers")
print("Customers table loaded successfully.")

orders_df = spark.table("orders")
print("Orders table loaded successfully.")

products_df = spark.table("products")
print("Products table loaded successfully.")

# Display preview

print("Displaying preview of Customers DataFrame")
display(customers_df)

print("Displaying preview of Orders DataFrame")
display(orders_df)

print("Displaying preview of Products DataFrame")
display(products_df)

# Writing to Bronze Layer (Delta Tables)
print("Writing raw data to Bronze layer...")

customers_df.write.format("delta").mode("overwrite").saveAsTable("bronze_customers")
print("bronze_customers table created successfully.")

orders_df.write.format("delta").mode("overwrite").saveAsTable("bronze_orders")
print("bronze_orders table created successfully.")

products_df.write.format("delta").mode("overwrite").saveAsTable("bronze_products")
print("bronze_products table created successfully.")

print("Bronze Layer ingestion completed successfully.")
