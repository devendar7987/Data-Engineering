# Silver Layer - Data Cleaning Process

print("Starting Silver Layer - Cleaning Process...")

# Read Bronze Tables

print("Reading Bronze tables...")

bronze_customers_df = spark.table("bronze_customers")
print("bronze_customers table loaded successfully.")

bronze_orders_df = spark.table("bronze_orders")
print("bronze_orders table loaded successfully.")

bronze_products_df = spark.table("bronze_products")
print("bronze_products table loaded successfully.")

# Print row counts before cleaning
print(f"Bronze Customers count: {bronze_customers_df.count()}")
print(f"Bronze Orders count: {bronze_orders_df.count()}")
print(f"Bronze Products count: {bronze_products_df.count()}")

# Apply Cleaning Rules

print("Applying cleaning transformations...")

# Remove duplicates and null values from customers
customers_clean = bronze_customers_df.dropDuplicates().dropna()
print("Customers cleaning completed.")

# Remove rows containing null values from orders
orders_clean = bronze_orders_df.dropna()
print("Orders cleaning completed.")

# Remove duplicate product records
products_clean = bronze_products_df.dropDuplicates()
print("Products cleaning completed.")

# Print row counts after cleaning
print(f"Silver Customers count: {customers_clean.count()}")
print(f"Silver Orders count: {orders_clean.count()}")
print(f"Silver Products count: {products_clean.count()}")

# Display Cleaned Data (Preview)

print("Displaying cleaned Customers DataFrame...")
display(customers_clean)

print("Displaying cleaned Orders DataFrame...")
display(orders_clean)

print("Displaying cleaned Products DataFrame...")
display(products_clean)

#  Write Cleaned Data to Silver Layer
print("Writing cleaned data to Silver layer...")

customers_clean.write.format("delta").mode("overwrite").saveAsTable("silver_customers")
print("silver_customers table created successfully.")

orders_clean.write.format("delta").mode("overwrite").saveAsTable("silver_orders")
print("silver_orders table created successfully.")

products_clean.write.format("delta").mode("overwrite").saveAsTable("silver_products")
print("silver_products table created successfully.")

print("Silver Layer processing completed successfully.")
