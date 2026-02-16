# Import Spark session and Spark SQL functions
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# Import pandas library
import pandas as pd

# Import time module for measuring execution time
import time

# Start timer
start_time = time.time()

# Create a Spark session for the project
spark = SparkSession.builder.appName("cleaning_orders_dataset_with_pyspark").getOrCreate()

# Load the parquet dataset into a Spark DataFrame
orders_data = spark.read.parquet("orders_data.parquet")

# Before cleansing metrics
print("\n===== BEFORE CLEANSING =====")
initial_count = orders_data.count()
print(f"Initial row count: {initial_count}")

# Preview the data without truncating long column values
print("Previewing the orders dataset (full column values):")
orders_data.show(truncate=False)

# Create a working copy of the original dataframe for cleaning
orders_data_clean = orders_data

# Create time_of_day column: "morning" (5am–12pm), "afternoon" (12pm–6pm), "evening" (6pm–12am); lower bound inclusive, upper bound exclusive
orders_data_clean = orders_data_clean.withColumn(
    "time_of_day",
    F.when((F.hour(F.col("order_date")) >= 5) & (F.hour(F.col("order_date")) <= 11), "morning")
    .when((F.hour(F.col("order_date")) >= 12) & (F.hour(F.col("order_date")) <= 17), "afternoon")
    .when((F.hour(F.col("order_date")) >= 18) & (F.hour(F.col("order_date")) <= 23), "evening")
    .otherwise(None)    
)
print("After creating time_of_day column (morning / afternoon / evening):")
orders_data_clean.show(truncate=False)


# Remove orders placed between 12am and 5am (inclusive) and convert timestamp column to date
orders_data_clean = orders_data_clean.filter(~(F.hour(F.col("order_date")).between(0,5)))
orders_data_clean = orders_data_clean.withColumn("order_date", F.to_date("order_date"))
print("After removing 12am–5am orders and converting timestamp to date:")
orders_data_clean.show(truncate=False)

# Remove rows where product contains "TV" and convert all values to lowercase
orders_data_clean = orders_data_clean.withColumn("product", F.lower(F.col("product")))
orders_data_clean = orders_data_clean.filter(~F.col("product").contains("tv"))
print("After removing TV-related products and converting product names to lowercase:")
orders_data_clean.show(truncate=False)

# Convert category values to lowercase
orders_data_clean = orders_data_clean.withColumn("category", F.lower(F.col("category")))
print("After converting category column to lowercase:")
orders_data_clean.show(truncate=False)

# New column containing the state from which the purchase was ordered
orders_data_clean = orders_data_clean.withColumn(
    "purchase_state",
    F.trim(F.split(F.col("purchase_address"), ",")[2]).substr(1,2)
)
print("After extracting purchase_state from address:")
orders_data_clean.show(truncate=False)

# After cleansing metrics

print("\n===== AFTER CLEANSING =====")
final_count = orders_data_clean.count()
print(f"Final cleaned row count: {final_count}")

# Estimate data volume
data_volume_mb = orders_data_clean.rdd.map(lambda row: len(str(row))).sum() / (1024 * 1024)
print(f"Approx data volume processed: {data_volume_mb:.2f} MB")

# Save the cleaned dataframe as a parquet file

# Convert Spark dataframe to Pandas
pdf = orders_data_clean.toPandas()

# Save using pandas
pdf.to_parquet("orders_data_clean.parquet", index=False)
print("Cleaned dataframe saved successfully as orders_data_clean.parquet")

# Reload the saved parquet file for validation
validated_df = pd.read_parquet("orders_data_clean.parquet")
print("Validation: Preview of saved parquet file")
print(validated_df.head())

print(f"Original cleaned row count: {final_count}")
print(f"Reloaded parquet row count: {len(validated_df)}")

# End timer
end_time = time.time()
total_time = end_time - start_time
print(f"\nTotal processing time: {total_time:.2f} seconds")