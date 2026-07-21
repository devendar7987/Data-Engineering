from pyspark.sql.functions import count, avg, round, col, sum

# Read transformed product data from the Silver layer
print("Reading data from the Silver layer in Amazon S3")

silver_df = spark.read.format("delta").load(
    "s3://product-data-pipeline-devendar/silver/products/"
)

print("Silver layer data loaded successfully")

# Generate product count by category
print("Generating product count by category")

gold_category_df = silver_df.groupBy("category").agg(
    count("*").alias("product_count")
)

display(gold_category_df)

# Generate average product rating by category
print("Generating average rating by category")

gold_rating_df = silver_df.groupBy("category").agg(
    round(avg("rating"), 2).alias("average_rating")
)

display(gold_rating_df)

# Generate product count by stock status
print("Generating stock status summary")

gold_stock_df = silver_df.groupBy("stock_status").agg(
    count("*").alias("product_count")
)

display(gold_stock_df)

# Retrieve the top 10 most expensive products
print("Retrieving top 10 most expensive products")

gold_top_products_df = silver_df.orderBy(
    col("product_price").desc()
).limit(10)

display(gold_top_products_df)

# Calculate the average discount percentage
print("Calculating average discount percentage")

gold_discount_df = silver_df.agg(
    round(avg("discount_percentage"), 2).alias("average_discount")
)

display(gold_discount_df)

# Calculate total stock quantity by category
print("Calculating total stock quantity by category")

gold_stock_quantity_df = silver_df.groupBy("category").agg(
    sum("stock").alias("total_stock")
)

display(gold_stock_quantity_df)


# Write analytical data to the Gold layer in Amazon S3
print("Writing analytical data to the Gold layer in Amazon S3")

gold_category_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/category_summary/"
)

gold_rating_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/category_rating/"
)

gold_stock_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/stock_summary/"
)

gold_top_products_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/top_expensive_products/"
)

gold_discount_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/discount_summary/"
)

gold_stock_quantity_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/gold/stock_quantity/"
)

print("Gold layer analytics written successfully to Amazon S3")

