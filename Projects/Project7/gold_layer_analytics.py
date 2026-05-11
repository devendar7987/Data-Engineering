# Loading Cleaned Data from the Silver Layer in Amazon S3, Performing Top Products Sales Analysis, and Storing the Result in the Gold Layer in Amazon S3


# Load Cleaned Silver Layer Datasets

print("Loading Cleaned Orders Dataset from Silver Layer")

orders_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_orders/"
)

print("Orders Dataset Loaded Successfully")


print("Loading Cleaned Products Dataset from Silver Layer")

products_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_products/"
)

print("Products Dataset Loaded Successfully")


# Create Spark SQL Temporary Views

print("Creating Temporary Views for SQL Analysis")

orders_df.createOrReplaceTempView("orders")

products_df.createOrReplaceTempView("products")

print("Temporary Views Created Successfully")


# Perform Top Products Sales Analysis using Spark SQL

print("Performing Top Products Sales Analysis")

top_products_df = spark.sql(
    """
    SELECT
        p.product_name,
        SUM(o.amount) AS total_sales
    FROM orders o
    JOIN products p
    ON o.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC
    """
)

print("Top Products Sales Analysis Completed Successfully")
print("Displaying Top Products Sales Dataset")
display(top_products_df)


# Write Top Products Sales Dataset to the Gold Layer in Amazon S3

print("Writing Top Products Sales Dataset to Gold Layer in Amazon S3")

top_products_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/gold/top_products/"
)

print("Top Products Sales Dataset Successfully Written to Gold Layer")