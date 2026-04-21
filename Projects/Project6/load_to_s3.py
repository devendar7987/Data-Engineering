# Data export layer: Load processed datasets from Delta and write them to S3 data lake in CSV format

# Set current database context
spark.sql("USE `ecommerce_data_pipeline_db`")

# Reading orders and customer summary data from Delta tables

print("Loading 'orders_detailed' table...")
orders_detailed_df = spark.table("orders_detailed")
print("'orders_detailed' table loaded successfully.")

print("Loading 'customer_summary' table...")
customer_summary_df = spark.table("customer_summary")
print("'customer_summary' table loaded successfully.")

# Writing processed datasets to S3 in Parquet format

print("Saving 'orders_detailed' data to S3...")

orders_detailed_df.write.format("csv").option("header", "true").mode("overwrite").save("s3://ecommerce-data-pipeline-devendar/processed/orders_detailed/")
print("'orders_detailed' data saved successfully.")


print("Saving 'customer_summary' data to S3...")

customer_summary_df.write.format("csv").option("header", "true").mode("overwrite").save("s3://ecommerce-data-pipeline-devendar/processed/customer_summary/")
print("'customer_summary' data saved successfully.")

print("Data export process completed successfully.")


# Validate S3 data by loading and inspecting sample records

print("Starting data validation: Reading datasets from S3...")

print("Loading 'orders_detailed' dataset from S3...")

orders_detailed_s3_df = spark.read.csv(
    "s3://ecommerce-data-pipeline-devendar/processed/orders_detailed/",
    header = True,
    inferSchema = True
)

print("'orders_detailed' dataset loaded successfully.")

print("Displaying sample records from 'orders_detailed' dataset:")
display(orders_detailed_s3_df.limit(20))


print("Loading 'customer_summary' dataset from S3...")

customer_summary_s3_df= spark.read.csv(
    "s3://ecommerce-data-pipeline-devendar/processed/customer_summary/",
    header = True,
    inferSchema = True
)

print("'customer_summary' dataset loaded successfully.")

print("Displaying sample records from 'customer_summary' dataset:")
display(customer_summary_s3_df.limit(20))




