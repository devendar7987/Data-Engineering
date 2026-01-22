# 🗄️ Project: Loading Single Table Data into Dimensions and Fact Table (Star Schema)

📂 **Location**  
Projects/Project2/

👨‍💻 **Author**  
**Devendar Thigulla**  
📅 Created on: **2026-01-21**

---

## ✨ Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** where data from a **single denormalized sales CSV file** is cleaned, transformed, and split into **dimension tables and a fact table**, then loaded into a **PostgreSQL data warehouse** using a **star schema** design.

In real-world analytics systems, transactional data usually arrives as flat files. For reporting, performance, and scalability, this data must be transformed into **dimension and fact tables**.

This project focuses on:

- Extracting sales data from a single CSV file
- Cleaning and standardizing the data
- Creating **dimension tables** (Customer, Product, Date)
- Creating a **fact table** (Sales)
- Loading data into PostgreSQL using SQLAlchemy
- Validating loaded data and foreign key relationships

---

## 📄 Dataset: `sales_raw.csv`

The raw dataset contains customer, product, and sales transaction data in a single table.

```
order_id,order_date,customer_id,customer_name,customer_city,product_id,product_name,category,price,quantity
1001,2024-01-10,C001,ravi,hyderabad,P101,laptop,electronics,55000,1
1002,2024-01-10,C002,anita,bangalore,P102,mouse,electronics,500,2
1003,2024-01-11,C001,ravi,hyderabad,P103,keyboard,electronics,,1
1004,2024-01-12,C003,rahul,chennai,P101,laptop,electronics,55000,
1005,2024-01-12,C002,anita,bangalore,P104,chair,furniture,7000,1
1006,2024-01-13,,sneha,pune,P105,desk,furniture,12000,1
```

---

## 🔄 ETL Process

### 1️⃣ Extract

- Reads the CSV file using **Pandas**
- Loads raw sales data into a DataFrame

---

### 2️⃣ Transform

- Converts `order_date` to datetime format
- Removes records with missing critical values
- Standardizes text columns (customer_name, customer_city, product_name, category)
- Ensures numeric data types for `quantity` and `price`

---

### 3️⃣ Dimensional Modeling (Star Schema)

#### 🟦 Dimension Tables

**dim_customer**

- customer_key (surrogate key)
- customer_id
- customer_name
- customer_city

**dim_product**

- product_key (surrogate key)
- product_id
- product_name
- category
- price

**dim_date**

- date_key (YYYYMMDD)
- order_date
- year
- month
- day

---

#### 🟨 Fact Table: `fact_sales`

Stores measurable sales data:

- fact_sales_key (surrogate key)
- date_key (FK)
- customer_key (FK)
- product_key (FK)
- quantity
- total_amount

---

## 4️⃣ Load (PostgreSQL)

- Uses **SQLAlchemy** to load data into PostgreSQL
- Dimension tables are loaded **before** the fact table
- Fact table enforces **foreign key relationships** with dimensions

---

## 🛢 Database

- **PostgreSQL**
- Tables:
  - dim_customer
  - dim_product
  - dim_date
  - fact_sales

---

## 📜 Scripts & Files

### 📌 Python ETL Script

- [`sales_dimensional_model_etl.py`](sales_dimensional_model_etl.py)

### 📌 SQL Schema File

- [`load_dimensions_and_fact.sql`](load_dimensions_and_fact.sql)

### 📌 Dataset

- [`sales_raw.csv`](sales_raw.csv)

---

## 📊 Result Output (Terminal)

ETL results are printed directly in the terminal, including:

- Extracted raw sales data from the CSV file
- Transformed and cleaned sales data
- Customer dimension table (`dim_customer`)
- Product dimension table (`dim_product`)
- Date dimension table (`dim_date`)
- Staging fact data after dimension key mapping
- Final fact table (`fact_sales`)
- Validation results from PostgreSQL tables
- Foreign key relationship checks between fact and dimension tables

---

## 🎯 Objectives

- Extract data from a single denormalized source
- Clean and standardize raw data
- Build a **star schema** using dimensions and facts
- Load data into PostgreSQL
- Validate referential integrity

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- pgAdmin

---

## 👨‍💻 Learning Source

This project was created as part of my **Data Engineering learning journey**, focusing on:

- ETL pipelines
- Dimensional data modeling
- Star schema design
- PostgreSQL integration with Python

⭐ If you found this project useful, feel free to explore more of my projects on GitHub!
