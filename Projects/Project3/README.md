# 🗄️ Project: Multi-Source Data Ingestion & Analytics Pipeline in Databricks

### 📌 Project Overview

Extracting structured data from multiple file formats (CSV, TSV, Excel) and loading it into Databricks for further processing and analytics.

📂 **Location**
Projects/Project3/

👨‍💻 **Author**  
**Devendar Thigulla**  
📅 Created on: **2026-02-23**

---

## ✨ Overview

This project demonstrates a complete **Data Engineering ETL pipeline in
Databricks**, where data from **multiple structured file formats (CSV,
TSV, Excel)** is extracted, transformed, and loaded into a **Medallion
Architecture (Bronze → Silver → Gold)** for analytics.

This project focuses on:

- Extracting data from multiple file types
- Handling missing values and removing duplicate records
- Cleaning and transforming datasets
- Implementing Medallion Architecture (Bronze, Silver, Gold)
- Performing analytical queries on the Gold layer
- Scheduling notebooks using Databricks Jobs

---

## 📄 Datasets Used

### 1️⃣ [customers.csv](customers.csv) (CSV Format)

| customer_id | name  | email           | city      |
| ----------- | ----- | --------------- | --------- |
| 1           | Ravi  | ravi@gmail.com  | Hyderabad |
| 2           | Anita | anita@gmail.com | Delhi     |
| 3           | Rahul | rahul@gmail.com | Mumbai    |

---

### 2️⃣ [orders.tsv](orders.tsv) (TSV Format)

| order_id | customer_id | product | amount |
| -------- | ----------- | ------- | ------ |
| 101      | 1           | Laptop  | 55000  |
| 102      | 2           | Mobile  | 20000  |
| 103      | 3           | Tablet  | 15000  |

---

### 3️⃣ [products.xlsx](products.xlsx) (Excel Format)

| product_id | product    | category    | price |
| ---------- | ---------- | ----------- | ----- |
| P1         | Laptop     | Electronics | 55000 |
| P2         | Mobile     | Electronics | 20000 |
| P3         | Tablet     | Electronics | 15000 |
| P4         | Headphones | Accessories | 3000  |

---

## 🏗️ Architecture: Medallion Design

This project follows the **Medallion Architecture**:

### 🥉 Bronze Layer — Raw Data Ingestion

Notebook: `bronze_ingestion.py`

- Reads raw source datasets (CSV, TSV, Excel)
- Loads data into Spark DataFrames
- Performs minimal validation and schema enforcement
- Stores raw data in Delta format for reliability and scalability
- Preserves original structure for downstream processing

Tables Created:

- `bronze_customers`
- `bronze_orders`
- `bronze_products`

---

### 🥈 Silver Layer — Data Cleaning & Transformation

Notebook: `silver_transformations.py`

- Reads Bronze Delta tables
- Removes null values and duplicate records
- Applies basic data quality validations
- Ensures consistent and clean datasets
- Writes transformed data to Silver layer

Tables Created:

- `silver_customers`
- `silver_orders`
- `silver_products`

---

### 🥇 Gold Layer — Analytics & Business Insights

Notebook: `gold_analytics.py`

- Reads cleaned Silver layer tables
- Performs business-level joins across customers, orders, and products
- Creates consolidated analytics dataset
- Stores curated data in `gold_retail_analytics` Delta table
- Executes aggregation queries for business insights (e.g., Total Sales by City)
- Generates final analytics output dataset (`gold_analytics.csv`)

---

## 🔄 ETL Flow

### 1️⃣ Extract

- Uploaded CSV, TSV, and Excel files into Databricks.
- Created tables from the uploaded files.
- Retrieved data from the created tables using PySpark.

---

### 2️⃣ Transform

- Removes duplicate records
- Removes null values
- Produces cleaned datasets for downstream processing

---

### 3️⃣ Load

- Data stored as Delta Tables
- Organized into Bronze, Silver, and Gold layers
- Queryable using Spark SQL

---

## 📜 Notebooks

### 📘 Databricks Scripts

- [`bronze_ingestion.py`](bronze_ingestion.py)
- [`silver_transformations.py`](silver_transformations.py)
- [`gold_analytics.py`](gold_analytics.py)

### 📊 Result Dataset

- [`gold_analytics.csv`](gold_analytics.csv)

---

## 🎯 Objectives

- Extract data from multiple structured formats
- Implement Medallion Architecture
- Perform scalable transformations using PySpark
- Build analytical layer for business reporting
- Automate execution using Databricks Job Scheduling

---

## 🛠️ Tools & Technologies

- Databricks (Community Edition)
- PySpark (Spark DataFrame API)
- Spark SQL
- Delta Lake (Delta Tables)

---

## 🚀 Key Learning Outcomes

- Multi-format data ingestion
- Data cleaning using Spark
- Implementing Bronze, Silver, Gold architecture
- Spark SQL analytics
- Job scheduling in Databricks

---

## 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**,
focusing on:

- End-to-end ETL pipelines
- Real-world file ingestion scenarios
- Data lake architecture
- Analytics engineering

⭐ Feel free to explore more of my projects on GitHub!
