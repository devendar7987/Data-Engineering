# 🤖 Project: AI-Powered E-commerce Data Engineering Platform

### 📌 Project Overview

Building an **E-commerce Data Engineering Platform** using **Amazon S3, Databricks, PySpark, Delta Lake, and Google Gemini AI**.

The project uses **Google Gemini AI** to convert natural language business questions into Spark SQL queries, execute them on e-commerce datasets in Databricks, and generate business insights.

📂 **Location**  
Projects/Project7/

👨‍💻 **Author**  
**Devendar Thigulla**  
📅 Created on: **2026-05-08**

---

# ✨ Overview

This project demonstrates a complete **Data Engineering pipeline** using Amazon S3, Databricks, PySpark, Delta Lake, and Google Gemini AI.

The project focuses on:

- Reading raw e-commerce datasets from Amazon S3
- Building Bronze, Silver, and Gold Delta Lake layers
- Performing data cleaning and transformations using PySpark
- Generating analytics datasets using Spark SQL
- Converting natural language questions into Spark SQL using Gemini AI
- Executing generated SQL queries automatically
- Generating business insights and recommendations
- Storing analytics and reports in Amazon S3

---

# 📄 Datasets Used

## 1️⃣ orders.csv

```csv
order_id,customer_id,product_id,amount,city,order_date
1,101,1001,50000,Hyderabad,2026-05-01
2,102,1002,30000,mumbai,2026-05-01
3,103,1003,,Delhi,2026-05-02
4,101,1002,35000,Hyderabad,2026-05-03
5,104,1001,-60000,Bangalore,2026-05-03
```

---

## 2️⃣ products.csv

```csv
product_id,product_name,category,price
1001,iPhone 15,Mobile,70000
1002,Samsung TV,electronics,50000
1003,MacBook Air,Laptop,
1003,MacBook Air,Laptop,
```

---

## 3️⃣ customers.csv

```csv
customer_id,customer_name,city
101,Rahul,Hyderabad
102,Priya,mumbai
103,Amit,
104,Sneha,Bangalore
104,Sneha,Bangalore
```

---

# 🏗️ Architecture: Data Engineering Design

This project follows a **Medallion Architecture**:

---

## 🥉 Bronze Layer — Data Ingestion

Script: `bronze_layer_ingestion.py`

- Reads raw CSV files from Amazon S3
- Infers schema automatically
- Stores raw datasets as Delta tables in Bronze Layer

Data Stored in Bronze Layer:

- bronze/orders
- bronze/products
- bronze/customers

---

## 🥈 Silver Layer — Data Cleaning & Transformation

Script: `silver_layer_transformation.py`

- Reads Bronze Layer Delta tables
- Cleans and standardizes datasets
- Removes duplicate records
- Handles null values
- Filters invalid records
- Standardizes categorical columns

### Transformations Applied

### Orders Dataset

- Remove duplicates
- Fill null amount values
- Remove negative sales amounts
- Standardize city names

### Products Dataset

- Remove duplicates
- Fill null prices
- Standardize category names

### Customers Dataset

- Remove duplicates
- Fill null city values
- Standardize city names

Cleaned Data Stored in Silver Layer:

- silver/cleaned_orders
- silver/cleaned_products
- silver/cleaned_customers

---

## 🥇 Gold Layer — Business Analytics

Script: `gold_layer_analytics.py`

- Reads cleaned Silver Layer datasets
- Performs analytics using Spark SQL
- Generates top products sales analysis
- Stores analytics datasets in Gold Layer

### Analytics Performed

- Product-wise sales analysis
- Revenue aggregation
- Top-selling product identification

Analytics Data Stored in Gold Layer:

- gold/top_products

---

## 🤖 NLP to SQL using Gemini AI

Script: `ai_text_to_sql.py`

- Reads cleaned Silver Layer datasets
- Creates Spark SQL temporary views
- Accepts natural language business questions
- Uses Gemini AI to generate Spark SQL queries
- Executes generated SQL automatically
- Stores analytics results in Gold Layer

### Example User Question

```text
Show top 3 products with highest number of orders
```

### Example Generated SQL

```sql
SELECT
    p.product_name,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_orders DESC
LIMIT 3
```

AI-Generated Analytics Stored in Gold Layer:

- gold/ai_top_ordered_products

---

## 🧠 Business Insights Layer

Script: `ai_business_insights.py`

- Reads analytics datasets from Gold Layer
- Converts Spark DataFrame into Pandas DataFrame
- Uses Gemini AI to generate business insights
- Produces recommendations and trend analysis
- Stores generated reports in Gold Layer

### Insights Generated

- Top ordered products summary
- Product ordering trends
- Business recommendations

AI-Generated Insights Stored in Gold Layer:

- gold/ai_business_reports

---

# 🔄 End-to-End Workflow

## 1️⃣ Extract

- Raw CSV files stored in Amazon S3
- Databricks reads datasets
- Bronze Layer Delta tables created

---

## 2️⃣ Transform

- Data cleaning using PySpark
- Null handling
- Duplicate removal
- Standardization
- Invalid data filtering

---

## 3️⃣ Load

- Cleaned datasets written to Silver Layer
- Spark analytics datasets written to Gold Layer
- AI-generated analytics results stored in Gold Layer using Gemini AI
- AI-generated business insights and reports stored in Gold Layer using Gemini AI

---

## 4️⃣ Processing

- Gemini AI converts English questions into Spark SQL
- Generated SQL executed automatically
- Results saved into Gold Layer

---

## 5️⃣ Business Insights

- Gemini AI analyzes analytics datasets
- Generates business summaries
- Creates recommendations and trends

---

## 📜 Notebooks

### 💻 Databricks Notebooks

- [`bronze_layer_ingestion.py`](bronze_layer_ingestion.py)
- [`silver_layer_transformation.py`](silver_layer_transformation.py)
- [`gold_layer_analytics.py`](gold_layer_analytics.py)
- [`ai_text_to_sql.py`](ai_text_to_sql.py)
- [`ai_business_insights.py`](ai_business_insights.py)

---

# 📊 Result Datasets

### Gold Analytics Output

- [gold_layer_analytics.csv](./gold_layer_analytics.csv)

### AI Text-to-SQL Analytics Output

- [ai_text_to_sql.csv](./ai_text_to_sql.csv)

### AI Business Insights Output

- [ai_business_insights.csv](./ai_business_insights.csv)

---

# 🎯 Objectives

- Build a Data Engineering pipeline
- Implement Medallion Architecture
- Integrate AWS S3 with Databricks
- Perform scalable data transformations using PySpark
- Implement NLP-to-SQL using Gemini AI
- Generate business insights
- Store analytics data using Delta Lake

---

# 🛠️ Tools & Technologies

- Amazon S3
- Databricks
- PySpark
- Spark SQL
- Delta Lake
- Google Gemini AI
- Python

---

# 🚀 Key Learning Outcomes

- Medallion Architecture implementation
- Delta Lake data engineering
- PySpark transformations
- Spark SQL analytics
- NLP to SQL generation
- Analytics systems development
- Business insight generation
- AWS S3 integration

---

# 💡 Example Business Questions

```text
Show top 3 products with highest number of orders

Show top selling products by revenue

Which category has highest sales

Show product-wise sales analysis
```

---

# 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**, focusing on:

- AI-powered analytics platforms
- Cloud Data Engineering
- NLP-based SQL generation
- Delta Lake architecture
- Databricks and PySpark processing

⭐ Feel free to explore more of my projects on GitHub!
