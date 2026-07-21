# 🗄️ Project: End-to-End Product Data Pipeline using Databricks & AWS

### 📌 Project Overview

Building a scalable **cloud-based Data Engineering pipeline** by
extracting product data from the **DummyJSON REST API**, processing it
in **Databricks using PySpark**, storing it in **Amazon S3** using the
**Medallion Architecture (Bronze, Silver, Gold)**, cataloging metadata
with **AWS Glue**, querying data using **Amazon Athena**, and
visualizing business insights using **Amazon QuickSight**.

📂 **Location**\
Projects/Project8/

👨‍💻 **Author**\
**Devendar Thigulla**

📅 **Created on:** 2026-07-20

------------------------------------------------------------------------

## 🏗️ Complete Project Architecture

- [View Complete Project Architecture](architecture/architecture.png)

------------------------------------------------------------------------

## ✨ Overview

This project demonstrates a complete **Data Engineering pipeline** built
on AWS.

This project focuses on:

-   Extracting product data from DummyJSON REST API
-   Building Bronze, Silver and Gold layers
-   Processing data using PySpark in Databricks
-   Storing Delta data in Amazon S3
-   Creating metadata using AWS Glue Data Catalog
-   Querying data using Amazon Athena
-   Building dashboards using Amazon QuickSight

------------------------------------------------------------------------

## 📄 Data Source

### DummyJSON Products API

``` text
https://dummyjson.com/products
```

------------------------------------------------------------------------

## 🏗️ Architecture: Product Data Pipeline

This project follows a **Medallion Architecture (Bronze → Silver →
Gold)**.

------------------------------------------------------------------------

### 🥉 Bronze Layer --- Databricks

**Script:** `bronze_ingestion.py`

-   Fetches product data from DummyJSON REST API
-   Creates Spark DataFrame
-   Stores raw data in Amazon S3 Bronze Layer

Output:

-   bronze/products/

------------------------------------------------------------------------

### 🥈 Silver Layer --- Databricks (PySpark)

**Script:** `silver_transformations.py`

-   Reads Bronze layer data
-   Cleans and standardizes the dataset
-   Creates business columns
-   Stores transformed data in Amazon S3 Silver Layer

Output:

-   silver/products/

------------------------------------------------------------------------

### 🥇 Gold Layer --- Databricks

**Script:** `gold_analytics.py`

Creates analytical datasets:

-   Category Summary
-   Category Rating
-   Stock Summary
-   Top Expensive Products
-   Discount Summary
-   Stock Quantity

Output:

-   gold/category_summary/
-   gold/category_rating/
-   gold/stock_summary/
-   gold/top_expensive_products/
-   gold/discount_summary/
-   gold/stock_quantity/

------------------------------------------------------------------------

## 🏆 AWS Glue

AWS Glue was used to register the analytical datasets stored in Amazon S3.

### Process

- Created a database named **product_analytics_db**
- Created tables manually inside the database
- Defined table names manually
- Configured each table to point to the corresponding Amazon S3 Gold Layer location

### Database

- product_analytics_db

---

## 📘 AWS Glue Data Catalog

AWS Glue Data Catalog was used to store the metadata of the analytical datasets.

### Process

- Defined the schema manually for each table
- Added column names and data types
- Stored metadata for all Gold Layer datasets
- Made the metadata available for Amazon Athena

### Tables Created

- category_summary
- category_rating
- stock_summary
- top_expensive_products
- discount_summary
- stock_quantity

---

## 🔍 Amazon Athena

Amazon Athena was used to query the analytical datasets stored in Amazon S3.

### Process

- Selected **AWSDataCatalog** as the data source
- Selected **product_analytics_db** as the database
- Athena automatically retrieved all tables from the AWS Glue Data Catalog
- Executed SQL queries on the analytical datasets
- Validated the query results before visualization

### Example Query

```sql
SELECT *
FROM "product_analytics_db"."category_summary";
```

---

## 📊 Amazon QuickSight

Amazon QuickSight was used to create interactive business dashboards.

### Process

- Selected **Amazon Athena** as the data source
- Imported analytical datasets from Athena
- Created interactive visualizations
- Generated business insights from the Gold Layer datasets

### Dashboards Created

- Product Count by Category
- Product Rating by Category
- Product Count by Stock Status
- Top 10 Most Expensive Products
- Average Product Discount (%)
- Total Stock Quantity by Category

---

## 🔄 AWS Analytics Workflow

```text
Amazon S3 (Gold Layer)
        │
        ▼
AWS Glue
(Database Creation)
        │
        ▼
AWS Glue Data Catalog
(Tables + Schema)
        │
        ▼
Amazon Athena
(SQL Queries)
        │
        ▼
Amazon QuickSight
(Business Dashboards)
```

------------------------------------------------------------------------

## 🔄 ETL Flow

### 1️⃣ Extract

-   Fetch data from DummyJSON API
-   Read into Databricks
-   Store in Bronze Layer

------------------------------------------------------------------------

### 2️⃣ Transform

-   Clean and standardize data
-   Create derived business columns
-   Store in Silver Layer

------------------------------------------------------------------------

### 3️⃣ Load

- Generate analytical datasets
- Store analytical data in Amazon S3 Gold Layer
- Create database, tables, and schema in AWS Glue
- Query analytical datasets using Amazon Athena
- Build business dashboards using Amazon QuickSight

------------------------------------------------------------------------

## 📜 Notebooks

### 📘 Databricks Scripts

-   [bronze_ingestion.py](notebooks/bronze_ingestion.py)
-   [silver_transformations.py](notebooks/silver_transformations.py)
-   [gold_analytics.py](notebooks/gold_analytics.py)

------------------------------------------------------------------------

## 📊 Dashboard Results

### 📘 Product Count by Category

- [product_count_by_category.png](results/product_count_by_category.png)

---

### 📘 Product Rating by Category

- [product_rating_by_category.png](results/product_rating_by_category.png)

---

### 📘 Product Count by Stock Status

- [product_count_by_stock_status.png](results/product_count_by_stock_status.png)

---

### 📘 Top 10 Most Expensive Products

- [top_10_expensive_products.png](results/top_10_expensive_products.png)

---

### 📘 Average Product Discount (%)

- [average_product_discount.png](results/average_product_discount.png)

---

### 📘 Total Stock Quantity by Category

- [total_stock_quantity_by_category.png](results/total_stock_quantity_by_category.png)

------------------------------------------------------------------------

## 🎯 Objectives

-   Build an end-to-end Data Engineering pipeline
-   Implement Medallion Architecture
-   Process data using PySpark
-   Create metadata using AWS Glue
-   Query data using Athena
-   Build dashboards using QuickSight

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

-   Python
-   PySpark
-   Databricks
-   Amazon S3
-   Delta Lake
-   AWS Glue Data Catalog
-   Amazon Athena
-   Amazon QuickSight
-   DummyJSON REST API

------------------------------------------------------------------------

## 🚀 Key Learning Outcomes

- REST API Integration
- Medallion Architecture
- PySpark Data Processing
- Delta Lake
- AWS Glue Data Catalog
- Amazon Athena Querying
- Amazon QuickSight Dashboard Development
- End-to-End Data Engineering Pipeline

------------------------------------------------------------------------

## 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**,
focusing on cloud-based ETL pipelines using Databricks and AWS.

⭐ Feel free to explore more of my Data Engineering projects on GitHub!
