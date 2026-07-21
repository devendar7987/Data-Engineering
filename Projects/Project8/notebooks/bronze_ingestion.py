import requests
import json
from pyspark.sql.functions import col

# Fetch data from API
url = "https://dummyjson.com/products"
response = requests.get(url)
print("API data fetched successfully")

# Convert response to Python dictionary
api_response = response.json()

# Extract products list
product_data = api_response["products"]
print(f"Retrieved {len(product_data)} products from the API.")

# Extract required product fields from the API response and prepare the data for Spark DataFrame creation
filtered_products = []

for product in product_data:
    filtered_products.append({
        "id" : product.get("id"),
        "title" : product.get("title"),
        "description": product.get("description"),
        "category": product.get("category"),
        "price": product.get("price"),
        "discount_percentage": float(product.get("discountPercentage")),
        "brand": product.get("brand"),
        "rating": product.get("rating"),
        "stock": product.get("stock"),
        "availability_status": product.get("availabilityStatus"),
        "product_width" : product.get("dimensions").get("width"),
        "product_height" : product.get("dimensions").get("height"),
        "product_depth" : product.get("dimensions").get("depth")
    })

print("Product data prepared successfully for Spark DataFrame creation")

# Create and display Spark DataFrame
bronze_products_df = spark.createDataFrame(filtered_products)
print("Spark DataFrame created successfully")

display(bronze_products_df)

# Write raw product data to the Bronze layer in Amazon S3
print("Writing raw product data to the Bronze layer in Amazon S3")

bronze_products_df.write.format("delta").mode("overwrite").save(
    "s3://product-data-pipeline-devendar/bronze/products/"
)

print("Bronze layer data written successfully to Amazon S3")
