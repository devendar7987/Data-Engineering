# Silver Layer - Data Cleaning Process

from pyspark.sql.functions import explode, col

# Set current database context
spark.sql("USE semi_structured_pipeline_db")

print("Starting Silver Layer - Cleaning Process...")

# Read Bronze Tables

print("Reading Bronze tables...")

bronze_orders_df = spark.table("bronze_orders")
print("bronze_orders table loaded successfully.")

bronze_products_df = spark.table("bronze_products")
print("bronze_products table loaded successfully.")

# Transform Orders (Explode JSON items)
print("Transforming orders data (Exploding items)...")

orders_exploded_df = bronze_orders_df.select(
    "order_id",
    explode("items").alias("items")
)

print("Preview after explode:")
display(orders_exploded_df)

# Flatten nested fields
orders_flattened_df = orders_exploded_df.select(
    "order_id",
    col("items.price").alias("order_price"),
    col("items.product").alias("product")
)

print("Flattened orders data:")
display(orders_flattened_df)
print("Orders transformation completed.")

# Transform Products Data

print("Transforming products data (Casting types)...")

products_standardized_df = bronze_products_df.select(
    col("id").cast("int").alias("id"),
    col("name"),
    col("price").cast("int").alias("product_price")
)

print("Standardized Products Data:")
display(products_standardized_df)
print("Products transformation completed.")

# Count Before Cleaning
print("Row counts before cleaning...")
print(f"Orders count before cleaning: {orders_flattened_df.count()}")
print(f"Products count before cleaning: {products_standardized_df.count()}")

# Apply Cleaning Rules

print("Applying cleaning transformations...")

# Remove duplicates from orders
orders_cleaned_df = orders_flattened_df.dropDuplicates()
print("Removed duplicate records from orders")

# Filter valid product prices
products_cleaned_df = products_standardized_df.filter(col("price") > 1500)
print("Filtered products where price > 1500")

# Count After Cleaning
print("Row counts after cleaning...")

# Print row counts after cleaning
print(f"Orders count after cleaning: {orders_cleaned_df.count()}")
print(f"Products count after cleaning: {products_cleaned_df.count()}")

# Display Cleaned Data

print("Displaying cleaned Orders DataFrame...")
display(orders_cleaned_df)

print("Displaying cleaned Products DataFrame...")
display(products_cleaned_df)

#  Write Cleaned Data to Silver Layer
print("Writing cleaned data to Silver layer...")

orders_cleaned_df.write.format("delta").mode("overwrite").saveAsTable("silver_orders")
print("silver_orders table created successfully.")

products_cleaned_df.write.format("delta").mode("overwrite").saveAsTable("silver_products")
print("silver_products table created successfully.")

print("Silver Layer processing completed successfully.")