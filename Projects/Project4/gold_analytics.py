# Databricks notebook source
# Gold Layer - Business Analytics Processing

from pyspark.sql.functions import sum

# Set current database context
spark.sql("USE semi_structured_pipeline_db")

print("Starting Gold Layer - Business Transformation Process...")

# Read Silver Tables

print("Reading Silver layer tables...")

silver_orders_df = spark.table("silver_orders")
print("silver_orders table loaded successfully.")

silver_products_df = spark.table("silver_products")
print("silver_products table loaded successfully.")

# Perform Business-Level Join
print("Performing join to create business analytics dataset...")
gold_product_sales_df = silver_orders_df.join(silver_products_df, silver_orders_df.product == silver_products_df.name, "inner")

print("Business transformation (join) completed successfully.")

# Print final row count
print(f"Gold dataset row count: {gold_product_sales_df.count()}")

# Display Final Output (Preview)
print("Preview of joined Gold Layer dataset...")
display(gold_product_sales_df)

#  Write Final Dataset to Gold Layer
print("Writing final dataset to Gold layer table...")

gold_product_sales_df.write.format("delta").mode("overwrite").saveAsTable("gold_product_sales")

print("gold_product_sales table created successfully.")

print("Gold Layer processing completed successfully.")



# Gold Layer - Sales Analytics Query

print("Starting Gold Layer Analytics: Fetching Product Sales Data...")

# Execute query on Gold table
gold_product_sales_summary_df = spark.sql("""
SELECT product, SUM(order_price) AS total_sales
FROM gold_product_sales
GROUP BY product
ORDER BY total_sales DESC
""")

print("Query executed successfully.")

# Display results
print("Displaying aggregated product-wise total sales from Gold Layer...")
display(gold_product_sales_summary_df)

print("Gold Layer Analytics completed successfully.")

