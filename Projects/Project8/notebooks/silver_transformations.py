from pyspark.sql.functions import upper, when, col, current_timestamp

# Read product data from the Bronze layer
print("Reading data from the Bronze layer in Amazon S3")

bronze_products_df = spark.read.format("delta").load(
    "s3://product-data-pipeline-devendar/bronze/products/"
)

print("Product data loaded successfully from Bronze layer")

# Remove duplicate records
print("Removing duplicate records")
silver_df = bronze_products_df.dropDuplicates()

# Fill missing values in the brand column
print("Filling missing values in the brand column")
silver_df = silver_df.fillna({
    "brand" : "Unknown"
})

# Standardize category values by converting them to uppercase
print("Standardizing category names")
silver_df = silver_df.withColumn(
    "category",
    upper(col("category"))
)

# Rename columns for better readability
print("Renaming columns")
silver_df = silver_df \
    .withColumnRenamed("id", "product_id") \
    .withColumnRenamed("title", "product_name") \
    .withColumnRenamed("description", "product_description") \
    .withColumnRenamed("brand", "brand_name") \
    .withColumnRenamed("price", "product_price")


# Create stock availability category
print("Creating stock status column")
silver_df = silver_df.withColumn(
    "stock_status",
    when(col("stock") < 20, "Low Stock")
    .when(col("stock") <= 50, "Medium Stock")
    .otherwise("High Stock")
)

# Categorize products based on price
print("Creating price category column")
silver_df = silver_df.withColumn(
    "price_category",
    when(col("product_price") < 100, "Budget")
    .when(col("product_price") < 500, "Mid Range")
    .otherwise("Premium")
)


# Add processing timestamp
print("Adding processing timestamp")
silver_df = silver_df.withColumn(
    "processed_timestamp",
    current_timestamp()
)

# Display transformed data
print("Displaying Silver layer data")
display(silver_df)

# Write transformed data to the Silver layer in Amazon S3
print("Writing transformed data to the Silver layer in Amazon S3")

silver_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/silver/products/"
)

print("Silver layer data written successfully to Amazon S3")
