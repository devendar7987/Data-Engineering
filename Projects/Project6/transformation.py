# Transformation layer: reads data from Delta tables, performs joins, data cleaning, and transformations

# Importing required PySpark SQL functions
from pyspark.sql.functions import col, when, concat, lit, count

# Set current database context
spark.sql("USE `ecommerce_data_pipeline_db`")

# Reading previously created Delta tables

print("Reading 'ingestion_orders' table...")
orders_df = spark.table("ingestion_orders")
print("'ingestion_orders' table loaded successfully.")

print("Reading 'ingestion_customers' table...")
customers_df = spark.table("ingestion_customers")
print("'ingestion_customers' table loaded successfully.")


# Join orders and customers data on customer_id

joined_df = orders_df.join(customers_df, on="customer_id", how="inner")
print("Join completed successfully.")

print("Displaying joined orders and customers data...")
display(joined_df)

# Remove rows with null values to clean the dataset

print("Removing rows with null values...")

before_count = joined_df.count()

cleaned_df = joined_df.dropna()

after_count = cleaned_df.count()

print(f"Rows before cleaning: {before_count}")
print(f"Rows after cleaning: {after_count}")
print(f"Rows removed: {before_count - after_count}")

print("Displaying cleaned dataset after removing null values...")
display(cleaned_df)

# Adding a new column 'order_category' based on 'order_status'

print("Starting transformation: Creating 'order_category' column...")

transformed_df = cleaned_df.withColumn(
    "order_category",
    when(col("order_status") == "delivered", "Completed")
    .when(col("order_status") == "shipped", "In Transit")
    .when(col("order_status") == "canceled", "Cancelled")
    .otherwise("Pending")
)

print("'order_category' column created successfully.")

print("Displaying sample records after transformation:")
display(transformed_df.select("order_status", "order_category").limit(20))

print("Category-wise count:")
display(transformed_df.groupBy("order_category").count())


# Adding a new column 'customer_key' by concatenating customer_city and customer_id with an underscore

print("Generating 'customer_key' by combining customer city and customer ID...")

orders_detailed_df = transformed_df.withColumn(
    "customer_key",
    concat(col("customer_city"), lit("_"), col("customer_id"))
)

print("'customer_key' column created successfully.")

print("Displaying sample records for customer_key validation:")
display(orders_detailed_df.select("customer_city", "customer_id", "customer_key").limit(20))

print("Displaying sample orders detailed data:")
display(orders_detailed_df.limit(20))

# Grouping data by customer_id, customer_city, and customer_state and calculating total number of orders per customer

print("Aggregating data to generate customer-level order summary...")

customer_summary_df = orders_detailed_df.groupBy(
    "customer_id", "customer_city", "customer_state",
).agg(
    count("order_id").alias("total_orders")
)

print("Customer summary aggregation completed successfully.")

print("Displaying sample customer summary data:")
display(customer_summary_df.limit(20))


# Writing transformed data to Delta tables for downstream analytics and reporting

print("Saving 'orders_detailed' table...")

orders_detailed_df.write.format("delta").mode("overwrite").saveAsTable("orders_detailed")
print("'orders_detailed' table saved successfully.")

print("Saving 'customer_summary' table...")

customer_summary_df.write.format("delta").mode("overwrite").saveAsTable("customer_summary")
print("'customer_summary' table saved successfully.")

print("Transformation completed successfully!")
