# Bronze Layer - Raw Data Ingestion

# Set current database context
spark.sql("USE semi_structured_pipeline_db")

print("Starting Bronze Layer - Raw Ingestion Process...")

# Reading source tables
print("Reading source tables...")

orders_df = spark.table("orders")
print("Orders table loaded successfully.")

products_df = spark.table("products")
print("Products table loaded successfully.")

# Display preview

print("Displaying preview of Orders DataFrame")
display(orders_df)

print("Displaying preview of Products DataFrame")
display(products_df)

# Writing to Bronze Layer (Delta Tables)
print("Writing raw data to Bronze layer...")

orders_df.write.format("delta").mode("overwrite").saveAsTable("bronze_orders")
print("bronze_orders table created successfully.")

products_df.write.format("delta").mode("overwrite").saveAsTable("bronze_products")
print("bronze_products table created successfully.")

print("Bronze Layer - Raw Ingestion Process completed successfully.")





