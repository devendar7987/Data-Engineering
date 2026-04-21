# Ingestion layer: reads raw data from S3 and loads it into Delta tables

# Read Orders Data from S3

print("Reading orders data from S3...")

orders_df = spark.read.csv(
    "s3://ecommerce-data-pipeline-devendar/raw/orders/",
    header = True,
    inferSchema = True
)

print("Orders Data Loaded Successfully")

print("Orders Data Schema:")
orders_df.printSchema()

print("Sample Orders Data:")
display(orders_df.limit(20))

print(f"Number of Orders: {orders_df.count()}")


# STEP 2: Read Customers Data from S3

print("Reading customers data from S3...")

customers_df = spark.read.csv(
    "s3://ecommerce-data-pipeline-devendar/raw/customers/",
    header = True,
    inferSchema = True
)

print("Customers Data Loaded Successfully")

print("Customers Data Schema:")
customers_df.printSchema()

print("Sample Customers Data:")
display(customers_df.limit(20))

print(f"Number of Customers: {customers_df.count()}")

# Set current database context
spark.sql("USE `ecommerce_data_pipeline_db`")

# Write raw data to Delta tables

print("Loading orders data into 'ingestion_orders' table...")

orders_df.write.format("delta").mode("overwrite").saveAsTable("ingestion_orders")
print(" 'ingestion_orders' table created successfully.")

print("Loading customers data into 'ingestion_customers' table...")

customers_df.write.format("delta").mode("overwrite").saveAsTable("ingestion_customers")
print(" 'ingestion_customers' table created successfully.")


            