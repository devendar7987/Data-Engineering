# Databricks notebook source
# Gold Layer - Business Analytics Processing

print("Starting Gold Layer - Business Transformation Process...")

# Read Silver Tables

print("Reading Silver layer tables...")

silver_customers_df = spark.table("silver_customers")
print("silver_customers table loaded successfully.")

silver_orders_df = spark.table("silver_orders")
print("silver_orders table loaded successfully.")

silver_products_df = spark.table("silver_products")
print("silver_products table loaded successfully.")

# Perform Business-Level Joins
print("Performing joins to create business analytics dataset...")

gold_retail_df = silver_orders_df.join(silver_customers_df, "customer_id").join(silver_products_df, "product")

print("Business transformation (joins) completed successfully.")

# Print final row count
print(f"Gold Retail Analytics row count: {gold_retail_df.count()}")

# Display Final Output (Preview)
print("Displaying Gold layer dataset preview...")
display(gold_retail_df)

#  Write Final Dataset to Gold Layer
print("Writing final dataset to Gold layer table...")
gold_retail_df.write.format("delta").mode("overwrite").saveAsTable("gold_retail_analytics")
print("gold_retail_analytics table created successfully.")

print("Gold Layer processing completed successfully.")



# Gold Layer - Sales Analytics Query

print("Running analytics query: Total Sales by City")

total_sales_df = spark.sql("""
SELECT city, SUM(amount) AS total_sales
FROM gold_retail_analytics
GROUP BY city
ORDER BY total_sales DESC                      
""")

print("Query executed successfully.")

# Display results
print("Displaying Total Sales by City...")
display(total_sales_df)