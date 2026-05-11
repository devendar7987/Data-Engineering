# Loading AI Top Ordered Products Data from Gold Layer, Converting Spark DataFrame to Pandas, Generating Business Insights using Gemini AI, and Writing AI Business Insights to Gold Layer in Amazon S3


# Import Gemini Library

from google import genai

print("Google Gemini AI Library Imported Successfully")


# Create Gemini Client

print("Creating Gemini AI Client Connection...")

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
)

print("Gemini AI Client Connected Successfully")


# Read AI Top Ordered Products Dataset from Gold Layer

ai_top_ordered_products_df = spark.read.format("delta").load(
    "s3://devendar-ecommerce-ai-data-lake/gold/ai_top_ordered_products/"
)

print("AI Top Ordered Products Dataset Loaded Successfully from Gold Layer")


# Convert Spark DataFrame to Pandas DataFrame

print("Converting Spark DataFrame to Pandas DataFrame")

pandas_df = ai_top_ordered_products_df.toPandas()

print("Conversion Completed Successfully")


# Create AI Insight Prompt

print("Creating Business Insight Prompt for Gemini AI")

insight_prompt = f"""
You are an Ecommerce Business Analyst.

Analyze the product order data below and provide a short business summary including:
1. Top ordered products
2. Key ordering trends
3. Short business recommendations

Keep the response concise and professional in under 150 words.

Product Order Data:
{pandas_df.to_string(index=False)}

"""

print("Prompt Created Successfully")


# Generate AI Business Insights

print("Generating AI Business Insights Using Gemini")

insight_response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents= insight_prompt
)

business_insights = insight_response.text

print("AI Business Insights Generated Successfully")

print("\nDisplaying Generated Business Insights")
print(business_insights)


# Create Spark DataFrame for Insights

print("Creating Spark DataFrame for AI Business Insights")

insights_df = spark.createDataFrame([
    {"business_insights": business_insights}

])

print("Insights DataFrame Created Successfully")

print("Displaying AI Business Insights DataFrame")
display(insights_df)


# Write AI Business Insights to Gold Layer in Amazon S3

print("Writing AI Generated Business Insights to Gold Layer in Amazon S3")

insights_df.write.format("delta").mode("overwrite").save(
    "s3://devendar-ecommerce-ai-data-lake/gold/ai_business_reports/"
)

print("AI Business Insights Successfully Written to Gold Layer")

