# Loading Cleaned Data from the Silver Layer in Amazon S3, Generating Spark SQL Queries using Google Gemini AI, Executing Queries using Spark SQL, and Storing AI Analytics Results in the Gold Layer in Amazon S3


# Import Gemini Library

from google import genai

print("Google Gemini AI Library Imported Successfully")


# Create Gemini Client

print("Creating Gemini AI Client Connection...")

client = genai.Client(
    api_key="AIzaSyCWCdRZ0S6tFdXBSY6oTdzZeL9Bu8DAl_E"
)

print("Gemini AI Client Connected Successfully")


# Load Cleaned Silver Layer Datasets

print("Loading Cleaned Orders Dataset from Silver Layer...")

orders_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_orders/"
)

print("Orders Dataset Loaded Successfully")


print("Loading Cleaned Products Dataset from Silver Layer...")

products_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_products/"
)

print("Products Dataset Loaded Successfully")


print("Loading Cleaned Customers Dataset from Silver Layer...")

customers_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/silver/cleaned_customers/"
)

print("Customers Dataset Loaded Successfully")


# Create Spark SQL Temporary Views

print("Creating Temporary Views for Spark SQL Queries...")

orders_df.createOrReplaceTempView("orders")

products_df.createOrReplaceTempView("products")

customers_df.createOrReplaceTempView("customers")

print("Temporary Views Created Successfully")


#  Define User Question

print("Defining User Business Question...")

user_question = "Show top 3 products with highest number of orders"

print(f"User Question: {user_question}")


# Define Dataset Schema for Gemini

schema = """
orders(
    order_id,
    customer_id,
    product_id,
    amount,
    city,
    order_date  
)

products(
    product_id,
    product_name,
    category,
    price 
)

customers(
    customer_id,
    customer_name,
    city  
)

"""

print("Schema Prepared Successfully")


# Create Gemini Prompt

print("Creating Prompt for Gemini AI SQL Generation...")

prompt = f"""
You are an expert Spark SQL generator.

Convert the user question into Spark SQL.

Return ONLY SQL query.

Schema:
{schema}

Question:
{user_question}

"""

print("Prompt Created Successfully")


# Generate SQL Query using Gemini AI

print("Generating Spark SQL Query using Gemini AI...")

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = prompt
)

generated_sql = response.text

print("SQL Query Generated Successfully")

print("\nGenerated SQL Query:")
print(generated_sql)


#  Clean Generated SQL Query

print("Cleaning Generated SQL Query...")

generated_sql = generated_sql.replace(
    "```sql", ""
).replace(
    "```", ""
).strip()

print("SQL Query Cleaned Successfully")

print("\nCleaned SQL Query:")
print(generated_sql)


# Execute Generated Spark SQL Query

print("Executing AI Generated Spark SQL Query...")

result_df = spark.sql(generated_sql)

print("SQL Query Executed Successfully")

print("Displaying AI Query Result...")
display(result_df)


# Write AI Query Result to the Gold Layer in Amazon S3

print("Writing AI Query Result to Gold Layer in Amazon S3...")

result_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/gold/ai_top_ordered_products/"
)

print("AI Query Result Successfully Written to Gold Layer")
