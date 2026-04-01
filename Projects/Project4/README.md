# 🗄️ Project: Semi-Structured Data Ingestion Pipeline (JSON & XML) using Databricks

### 📌 Project Overview

Extracting semi-structured data from JSON and XML files and building a scalable ETL pipeline in Databricks for processing and analytics.

📂 **Location**  
Projects/Project4/

👨‍💻 **Author**  
**Devendar Thigulla**  
📅 Created on: **2026-03-31**

---

## ✨ Overview

This project demonstrates a complete **Data Engineering ETL pipeline in Databricks**, where data from **semi-structured file formats (JSON, XML)** is extracted, transformed, and loaded into a **Medallion Architecture (Bronze → Silver → Gold)** for analytics.

This project focuses on:

- Extracting data from JSON and XML files  
- Handling nested and hierarchical data structures  
- Flattening JSON arrays using PySpark  
- Understanding XML schema (XSD concept)  
- Cleaning and transforming datasets  
- Implementing Medallion Architecture (Bronze, Silver, Gold)  
- Performing analytical queries on the Gold layer  

---

## 📄 Datasets Used

### 1️⃣ orders.json (JSON Format)

```json
{
  "order_id": 101,
  "customer": "Devendar",
  "items": [
    {"product": "Laptop", "price": 50000},
    {"product": "Mouse", "price": 500}
  ]
}
```

---

### 2️⃣ products.xml (XML Format)

```xml
<products>
   <product>
      <id>1</id>
      <name>Laptop</name>
      <price>50000</price>
   </product>
</products>
```

---

## 🏗️ Architecture: Medallion Design

This project follows the **Medallion Architecture**:

---

### 🥉 Bronze Layer — Raw Data Ingestion

Notebook: `bronze_ingestion.py`

- Reads raw JSON and XML tables
- Loads data into Spark DataFrames
- Performs minimal validation
- Stores raw data in Delta format
- Preserves original structure for downstream processing

Tables Created:

- `bronze_orders`
- `bronze_products`

---

### 🥈 Silver Layer — Data Cleaning & Transformation

Notebook: `silver_transformations.py`

- Reads Bronze Delta tables  
- Flattens nested JSON using `explode()`  
- Extracts required fields from complex structures  
- Applies schema standardization (XSD concept via casting)  
- Removes duplicates and invalid records  
- Writes cleaned data to Silver layer  

Tables Created:

- `silver_orders`
- `silver_products`

---

### 🥇 Gold Layer — Analytics & Business Insights

Notebook: `gold_analytics.py`

- Reads cleaned Silver layer tables  
- Performs joins between orders and products  
- Creates business-level analytics dataset  
- Stores curated data in `gold_product_sales`  
- Executes aggregation queries (Total Sales by Product)  

---

## 🔄 ETL Flow

### 1️⃣ Extract

- Uploaded JSON and XML files into Databricks  
- Created tables from uploaded files  
- Retrieved data using PySpark  

---

### 2️⃣ Transform

- Flatten nested JSON structures  
- Cast data types for XML schema consistency  
- Remove duplicate records  
- Filter invalid values  

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

---

## 🧠 XSD Concept (XML Schema Definition)

👉 Detailed explanation available in:  
📄 **[`xsd_schema_concept.md`](xsd_schema_concept.md)**  


---

## 📊 Result Dataset

- [`gold_analytics.csv`](gold_analytics.csv)  
- Contains aggregated product-level sales insights  
- Generated from Gold layer using Spark SQL


## 🎯 Objectives

- Extract data from semi-structured formats  
- Handle nested JSON data  
- Understand and apply XML schema concepts (XSD)  
- Implement Medallion Architecture  
- Perform scalable transformations using PySpark  
- Build analytical datasets for reporting  

---

## 🛠️ Tools & Technologies

- Databricks (Community Edition)  
- PySpark (Spark DataFrame API)  
- Spark SQL  
- Delta Lake (Delta Tables)  

---

## 🚀 Key Learning Outcomes

- Semi-structured data ingestion  
- JSON flattening using `explode()`  
- XML processing and schema handling  
- Data cleaning with PySpark  
- Implementing Bronze, Silver, Gold architecture  
- Building analytics datasets  

---

## 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**, focusing on:

- End-to-end ETL pipelines  
- Semi-structured data processing  
- Data lake architecture  
- Analytics engineering  

⭐ Feel free to explore more of my projects on GitHub!
