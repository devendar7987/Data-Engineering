# Loading Data from the Bronze Layer in Amazon S3, Cleaning the Data, and Storing it in the Silver Layer in Amazon S3


# Importing All Required PySpark SQL Functions

from pyspark.sql.functions import *


# Reading Orders Dataset from Bronze Layer in Amazon S3

print("Loading Orders Dataset from Bronze Layer")

orders_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/bronze/orders/"
)

print("Orders Dataset Loaded Successfully")


# Reading Products Dataset from Bronze Layer in Amazon S3

print("Loading Products Dataset from Bronze Layer")

products_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/bronze/products/"
)

print("Products Dataset Loaded Successfully")


# Reading Customers Dataset from Bronze Layer in Amazon S3

print("Loading Customers Dataset from Bronze Layer")

customers_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/bronze/customers/"
)

print("Customers Dataset Loaded Successfully")


print("Starting Data Cleaning and Transformation Process")

# Cleaning Orders Dataset

print("Removing Duplicate Records from Orders Dataset")

clean_orders_df = orders_df.dropDuplicates()

print("Filling Null Values in Amount Column")

clean_orders_df = clean_orders_df.fillna({
    "amount":0
})

print("Filtering Invalid Amount Values")

clean_orders_df = clean_orders_df.filter(
    col("amount") >= 0
)

print("Standardizing City Column Format")

clean_orders_df = clean_orders_df.withColumn(
    "city",
    initcap(col("city"))
)

print("Orders Dataset Cleaning Completed Successfully")
print("Displaying Cleaned Orders Dataset")
display(clean_orders_df)


# Cleaning Products Dataset

print("Removing Duplicate Records from Products Dataset")

clean_products_df = products_df.dropDuplicates()

print("Filling Null Values in Price Column")

clean_products_df = clean_products_df.fillna({
    "price":0
})

print("Standardizing Category Column Format")

clean_products_df = clean_products_df.withColumn(
    "category",
    initcap(col("category"))
)

print("Products Dataset Cleaning Completed Successfully")
print("Displaying Cleaned Products Dataset")
display(clean_products_df)


# Cleaning Customers Dataset

print("Removing Duplicate Records from Customers Dataset")

clean_customers_df = customers_df.dropDuplicates()

print("Filling Null Values in City Column")

clean_customers_df = clean_customers_df.fillna({
    "city": "Unknown"
})

print("Standardizing City Column Format")

clean_customers_df = clean_customers_df.withColumn(
    "city",
    initcap(col("city"))
)

print("Customers Dataset Cleaning Completed Successfully")
print("Displaying Cleaned Customers Dataset")
display(clean_customers_df)


# Writing Cleaned Orders, Products, and Customers datasets into the Silver Layer in Amazon S3

print("Writing Cleaned Orders Dataset to Silver Layer in Amazon S3")

clean_orders_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_orders/"
)

print("Cleaned Orders Dataset Successfully Written to Silver Layer")


print("Writing Cleaned Products Dataset to Silver Layer in Amazon S3")

clean_products_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_products/"
)

print("Cleaned Products Dataset Successfully Written to Silver Layer")


print("Writing Cleaned Customers Dataset to Silver Layer in Amazon S3")

clean_customers_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_customers/"
)

print("Cleaned Customers Dataset Successfully Written to Silver Layer")

print("All Cleaned Datasets Successfully Written to the Silver Layer in Amazon S3")


