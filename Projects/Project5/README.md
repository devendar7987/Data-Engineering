# 🗄️ Project: Batch Data Pipeline with Runtime Analysis using AWS S3 and Snowflake

### 📌 Project Overview

Building a scalable **Full Load ETL pipeline** by loading large datasets (1M+ records) from **Amazon S3 into Snowflake** using external stages and tracking execution runtime.

📂 **Location**  
Projects/Project5/

👨‍💻 **Author**  
**Devendar Thigulla**  
📅 Created on: **2026-04-09**

---

## ✨ Overview

This project demonstrates a complete **Data Engineering ETL pipeline using Amazon S3 and Snowflake**, where large-scale structured data is generated, stored, and loaded into a cloud data warehouse.

This project focuses on:

- Generating large datasets (1M+ records) using Python
- Uploading data into Amazon S3
- Creating secure Storage Integration between S3 and Snowflake
- Using External Stages for data ingestion
- Performing Full Load (Batch Load) using COPY INTO
- Tracking runtime using Snowflake Query History
- Validating data load performance

---

## 📄 Datasets Used

### 1️⃣ customers.csv

customer_id,name,city  
1,Sai,Hyderabad  
2,Amit,Mumbai

---

### 2️⃣ orders.csv

order_id,customer_id,amount  
1,101,2500  
2,102,3200

---

### 3️⃣ payments.csv

payment_id,order_id,status  
1,201,SUCCESS  
2,202,FAILED

---

## 🏗️ Architecture: Batch Processing Design

This project follows a **Batch Processing Architecture**:

---

### 🥉 Data Generation Layer

Script: [files_creation.py](files_creation.py)

- Generates 1M+ records using Python (Pandas, NumPy)
- Creates structured CSV datasets
- Simulates real-world large-scale data

Files Created:

- [customers.csv](customers.csv)
- [orders.csv](orders.csv)
- [payments.csv](payments.csv)

---

### 🥈 Storage Layer — Amazon S3

- Stores raw CSV files in S3 bucket
- Organizes data into folders (customers, orders, payments)
- Acts as a data lake for ingestion

---

### 🥇 Data Warehouse Layer — Snowflake

SQL Scripts:

- `setup.sql` → Database & Schema creation
- `tables.sql` → Table definitions
- `stage.sql` → Storage integration & stages
- `load.sql` → Full load execution

---

## 🔄 ETL Flow

### 1️⃣ Extract

- Generated CSV files using Python
- Uploaded files into Amazon S3 bucket
- Organized data into structured folders

---

### 2️⃣ Transform

- Minimal transformation (Full Load approach)
- Schema defined in Snowflake tables
- Data mapped during loading

---

### 3️⃣ Load

- Used `COPY INTO` command
- Loaded data from external stages into Snowflake
- Implemented Full Load using TRUNCATE + LOAD

---

## 📜 SQL Scripts

### 📘 Setup Script

- [setup.sql](setup.sql)
- Creates database and schema

---

### 📘 Tables Script

- [tables.sql](tables.sql)
- Defines customers, orders, payments tables

---

### 📘 Stage Script

- [stage.sql](stage.sql)
- Creates Storage Integration
- Connects Snowflake to S3
- Defines External Stages

---

### 📘 Load Script

- [load.sql](load.sql)
- Performs Full Load (TRUNCATE + COPY INTO)
- Validates row counts
- Calculates runtime

---

## 📊 Result Dataset

- Fully loaded Snowflake tables
- Each table contains **1M+ records**
- Data validated using COUNT queries
- Total data load runtime calculated using Snowflake Query History
- Runtime measured in seconds to evaluate pipeline performance

---

## 🎯 Objectives

- Implement Full Load ETL pipeline
- Integrate Amazon S3 with Snowflake
- Load large datasets (1M+ records) efficiently
- Track query runtime and performance
- Understand batch processing workflows

---

## 🛠️ Tools & Technologies

- Amazon S3
- Snowflake
- Python (Pandas, NumPy)
- Snowflake SQL

---

## 🚀 Key Learning Outcomes

- Full Load vs Incremental Load concepts
- Snowflake External Stage usage
- Storage Integration with IAM Role
- COPY INTO for bulk data loading
- Query performance monitoring
- Handling large-scale datasets

---

## 👨‍💻 Learning Source

This project is part of my **Data Engineering learning journey**, focusing on:

- Cloud-based ETL pipelines
- Batch data processing
- Data warehouse integration
- Performance optimization

⭐ Feel free to explore more of my projects on GitHub!
