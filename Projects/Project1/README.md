# 🗄️ Project: Loading Single Table Data into Parent and Child Tables

📂 **Location**  
Projects/Project1/

👨‍💻 **Author**  
Devendar Thigulla  
📅 Created on: 2026-01-07

---

## ✨ Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline where data from a single denormalized CSV file is cleaned, transformed, and split into a parent table and multiple child tables, then loaded into a PostgreSQL database.

In real-world data engineering systems, source files often arrive as flat tables containing mixed information. For efficient storage, scalability, and analytics, this data must be normalized into relational tables.

This project focuses on:

- Extracting employee data from a single CSV file
- Cleaning and transforming the data
- Splitting the data into one parent table and multiple child tables
- Loading the results into PostgreSQL using SQLAlchemy
- Validating loaded data using SQL queries

---

## 📄 Dataset: employee_raw.csv

The raw dataset contains employee, salary, project, and contact details in one table.

```
emp_id,emp_name,dept,salary,project,project_hours,address,phone
101,Ravi Kumar,IT,75000,ERP System,120,Hyderabad,9876543210
102,Sita Sharma,IT,55000,Website Revamp,95,Bengaluru,9876543211
103,Arjun Reddy,HR,60000,Recruitment Drive,80,Warangal,9876543212
104,Neha Singh,HR,0,Training Program,60,Delhi,9876543213
105,Amit Verma,Finance,80000,Budget Analysis,110,Mumbai,9876543214
106,Pooja Nair,Finance,45000,Audit Prep,70,Kochi,9876543215
102,Sita Sharma,IT,55000,Website Revamp,95,Bengaluru,9876543211
```

---

## 🔄 ETL Process

### 1️⃣ Extract

Reads the CSV file using Pandas and loads raw employee data.

### 2️⃣ Transform

- Removes duplicate records
- Filters out records with invalid salary values (salary ≤ 0)

### 3️⃣ Normalize Data

#### 🟦 Parent Table: employees

Stores core employee information:

- emp_id
- emp_name
- dept

#### 🟩 Child Tables

- employee_salary (salary details)
- employee_projects (project assignments)
- employee_contact (contact details)

---

## 4️⃣ Load (PostgreSQL)

Uses SQLAlchemy to load parent and child tables into PostgreSQL.  
Tables are replaced if they already exist.

---

## 🛢 Database

- PostgreSQL
- Tables:
  - employees
  - employee_salary
  - employee_projects
  - employee_contact

---

## 📜 Script & Result Output

### Script

- [employee_etl_pipeline.py](employee_etl_pipeline.py)

### Result Output

ETL results are printed directly in the terminal, including:

- Extracted raw data
- Transformed data after cleaning
- Parent table (employees)
- Child tables (employee_salary, employee_projects, employee_contact)
- Validation queries from PostgreSQL tables

---

## 🎯 Objectives

- Extract data from a single raw source
- Clean and filter invalid records
- Normalize data into parent–child structure
- Load data into PostgreSQL
- Validate the loaded data

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- pgAdmin

---

## 👨‍💻 Learning Source

This project was created as part of my Data Engineering learning journey, focusing on ETL pipelines and relational data modeling.

⭐ If you found this project useful, explore more of my projects on GitHub!
