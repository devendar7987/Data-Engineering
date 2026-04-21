# 🗄️ Project: End-to-End ETL Pipeline using S3, Databricks, and Snowflake

### 📌 Project Overview

Building a scalable **ETL data pipeline** by ingesting raw datasets from **Amazon S3**, processing them in **Databricks using PySpark**, and loading transformed data into **Snowflake** for analytics.

📂 **Location**
Projects/Project6/

👨‍💻 **Author**
**Devendar Thigulla**
📅 Created on: **2026-04-19**

---

## ✨ Overview

This project demonstrates a complete **Data Engineering ETL pipeline using Amazon S3, Databricks, and Snowflake**, where structured e-commerce datasets are processed and analyzed.

This project focuses on:

- Reading raw data from Amazon S3
- Loading data into Databricks Delta tables
- Performing data transformation using PySpark
- Writing processed data back to S3
- Integrating Snowflake with S3 using Storage Integration
- Loading data using External Stages and COPY INTO
- Running analytical queries on processed datasets

---

## 📄 Datasets Used

### 1️⃣ customers.csv

```csv
customer_id,customer_unique_id,customer_zip_code_prefix,customer_city,customer_state
06b8999e2fba1a1fbc88172c00ba8bc7,861eff4711a542e4b93843c6dd7febb0,14409,franca,SP
18955e83d337fd6b2def6b18a428ac77,290c77bc529b7ac935b93aa66c333dc3,09790,sao bernardo do campo,SP
4e7b3e00288586ebd08712fdd0374a03,060e732b5b29e8181a18229c7b0b2b5e,01151,sao paulo,SP
b2b6027bc5c5109e529d4dc6358b12c3,259dac757896d24d7702b9acbbff3f3c,08775,mogi das cruzes,SP
```

---

### 2️⃣ orders.csv

```csv
order_id,customer_id,order_status,order_purchase_timestamp,order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,order_estimated_delivery_date
e481f51cbdc54678b7cc49136f2d6af7,9ef432eb6251297304e76186b10a928d,delivered,2017-10-02 10:56:33,2017-10-02 11:07:15,2017-10-04 19:55:00,2017-10-10 21:25:13,2017-10-18 00:00:00
53cdb2fc8bc7dce0b6741e2150273451,b0830fb4747a6c6d20dea0b8c802d7ef,delivered,2018-07-24 20:41:37,2018-07-26 03:24:27,2018-07-26 14:31:00,2018-08-07 15:27:45,2018-08-13 00:00:00
47770eb9100c2d0c44946d9cf07ec65d,41ce2a54c0b03bf3443c3d931a367089,delivered,2018-08-08 08:38:49,2018-08-08 08:55:23,2018-08-08 13:50:00,2018-08-17 18:06:29,2018-09-04 00:00:00
949d5b44dbf5de918fe9c16f97b45f8a,f88197465ea7920adcdbec7375364d82,delivered,2017-11-18 19:28:06,2017-11-18 19:45:59,2017-11-22 13:39:59,2017-12-02 00:28:42,2017-12-15 00:00:00
```

---

## 🏗️ Architecture: ETL Processing Design

This project follows a **Layered ETL Architecture**:

---

### 🥉 Ingestion Layer — Databricks

Script: ingestion.py

- Reads raw CSV data from S3
- Infers schema automatically
- Loads data into Delta tables

Tables Created:

- ingestion_orders
- ingestion_customers

---

### 🥈 Transformation Layer — Databricks (PySpark)

Script: transformation.py

- Joins orders and customers datasets
- Cleans data using dropna()
- Applies conditional logic
- Creates derived columns
- Performs aggregation

Transformations:

- JOIN → customer_id
- Data Cleaning → dropna()
- CONDITION → order_category
- CONCAT → customer_key
- Aggregation → total_orders

Tables Created:

- orders_detailed
- customer_summary

---

### 🥇 Export Layer — S3

Script: load_to_s3.py

- Reads Delta tables
- Writes processed data to S3

Output:

- processed/orders_detailed/
- processed/customer_summary/

---

### 🏆 Data Warehouse Layer — Snowflake

SQL Scripts:

- `setup.sql` → Database and schema creation
- `tables.sql` → Table definitions
- `stage.sql` → Storage integration and external stage setup
- `load.sql` → Full data load

---

## 🔄 ETL Flow

### 1️⃣ Extract

- Data stored in Amazon S3
- Read into Databricks
- Loaded into Delta tables

---

### 2️⃣ Transform

- Data joined and cleaned
- Business logic applied
- Aggregation performed

---

### 3️⃣ Load

- Data written back to S3 from Databricks
- Data retrieved from S3 into Snowflake
- External stage created in Snowflake
- Data loaded using COPY INTO

---

## 📜 Notebooks

### 📘 Databricks Scripts

- [`ingestion.py`](ingestion.py)
- [`transformation.py`](transformation.py)
- [`load_to_s3.py`](load_to_s3.py)

---

## 📜 SQL Scripts

### 📘 Setup Script

- [setup.sql](setup.sql)
- Creates database and schema

---

### 📘 Tables Script

- [tables.sql](tables.sql)
- Defines ORDERS_DETAILED and CUSTOMER_SUMMARY tables

---

### 📘 Stage Script

- [stage.sql](stage.sql)
- Creates storage integration
- Connects Snowflake to S3
- Defines external stages

---

### 📘 Load Script

- [load.sql](load.sql)
- Performs Full Load (TRUNCATE + COPY INTO)
- Retrieves records for validation
- Applies customer segmentation logic

---

## 📊 Result Dataset

- [snowflake_query_results.csv](snowflake_query_results.csv)
- Cleaned dataset in Databricks
- Transformed into Delta tables
- Stored in S3
- Loaded into Snowflake using COPY INTO
- Analytical query executed

---

## 🎯 Objectives

- Build end-to-end ETL pipeline
- Integrate S3, Databricks, Snowflake
- Perform PySpark transformations
- Enable analytics using Snowflake

---

## 🛠️ Tools & Technologies

- Amazon S3
- Databricks
- PySpark
- Delta Lake
- Snowflake

---

## 🚀 Key Learning Outcomes

- ETL pipeline design
- Delta tables usage
- PySpark transformations
- Snowflake integration
- COPY INTO loading

---

## 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**, focusing on:

- Cloud ETL pipelines
- Data processing at scale
- Data warehouse integration

⭐ Feel free to explore more of my projects on GitHub!
