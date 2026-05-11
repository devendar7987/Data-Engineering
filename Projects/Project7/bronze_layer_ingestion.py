# Reading Raw Data from Amazon S3 and Writing Data to the Bronze Layer in Amazon S3

# Reading Orders Dataset from Amazon S3

print("Loading Orders Dataset from S3")

orders_df = spark.read.csv(
    "s3://devendar-ecommerce-ai-data-lake/raw/orders/orders.csv",
    header=True,
    inferSchema=True
)

print("Orders Dataset Loaded Successfully")
print("Displaying Orders Dataset")
display(orders_df)


# Reading Products Dataset from Amazon S3

print("Loading Products Dataset from S3")

products_df = spark.read.csv(
    "s3://devendar-ecommerce-ai-data-lake/raw/products/products.csv",
    header=True,
    inferSchema=True
)

print("Products Dataset Loaded Successfully")
print("Displaying Products Dataset")
display(products_df)


# Reading Customers Dataset from Amazon S3

print("Loading Customers Dataset from S3")

customers_df = spark.read.csv(
    "s3://devendar-ecommerce-ai-data-lake/raw/customers/customers.csv",
    header=True,
    inferSchema=True
)

print("Customers Dataset Loaded Successfully")
print("Displaying Customers Dataset")
display(customers_df)


# Writing Orders, Products, and Customers datasets into the Bronze Layer in Amazon S3

print("Writing Orders Dataset to Bronze Layer in Amazon S3")

orders_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/bronze/orders/"
)

print("Orders Dataset Successfully Written to Bronze Layer")


print("Writing Products Dataset to Bronze Layer in Amazon S3")

products_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/bronze/products/"
)

print("Products Dataset Successfully Written to Bronze Layer")


print("Writing Customers Dataset to Bronze Layer in Amazon S3")

customers_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/bronze/customers/"
)

print("Customers Dataset Successfully Written to Bronze Layer")

print("All Datasets Successfully Loaded into the Bronze Layer in Amazon S3")





