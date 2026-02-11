# 🧾 Project: Cleaning an Orders Dataset with PySpark

## 📂 Location

`Python/Cleaning an Orders Dataset with PySpark/`

## 👨‍💻 Author

**Devendar Thigulla**
📅 _Created on_: 2026-02-09

---

## ✨ Overview

This project focuses on cleaning and preprocessing an e-commerce orders dataset for **Voltmart**, an electronics retail company.

The Machine Learning team requested a clean dataset to build a **demand forecasting model**. The raw dataset contains order records from the previous year and requires multiple transformations to match a standardized format.

Using **PySpark**, the dataset is filtered, transformed, and enriched with new features to produce a high-quality analytics-ready table.

---

## 📄 Dataset

**Source file:** `orders_data.parquet`

The dataset contains detailed order records including timestamps, product details, pricing, profitability, and purchase location.

---

## 🎯 Objectives

- Remove invalid or unwanted orders
- Standardize text formatting
- Extract time-based features
- Create new derived columns
- Ensure consistency for ML modeling
- Validate final output after saving
- Export cleaned dataset as parquet

---

## 🧩 Cleaning Requirements Implemented

| Column           | Action Taken                                                           |
| ---------------- | ---------------------------------------------------------------------- |
| `order_date`     | Removed orders placed between **12am–5am**; converted timestamp → date |
| `time_of_day`    | New column: morning (5–12), afternoon (12–6), evening (6–12)           |
| `product`        | Removed rows containing “TV”; converted to lowercase                   |
| `category`       | Converted to lowercase                                                 |
| `purchase_state` | Extracted state from purchase address                                  |

---

## 🔄 Process Overview

### 1. Extract

Loaded the parquet dataset into a Spark DataFrame.

### 2. Transform

- Filtered early-morning orders
- Created `time_of_day` classification
- Cleaned text fields
- Removed discontinued products
- Extracted US state from address
- Converted timestamps to date format

### 3. Load

Saved the cleaned dataset as:

```
orders_data_clean.parquet
```

### 4. Validate

- Reloaded the saved parquet file
- Compared row counts with cleaned dataframe
- Verified preview and dataset structure

---

## 🛠️ Tools & Technologies

- **PySpark** → Distributed data processing
- **Pandas** → Local parquet export
- **Python 3.10+** → Used to implement the cleaning workflow
- **Spark SQL functions** → Data transformation & cleaning

Key techniques used:

- Timestamp filtering
- Conditional column generation
- String normalization
- Column extraction
- Dataset validation

---

## 📜 Script & Result Datasets

- [orders_data_cleaning_pyspark.py](orders_data_cleaning_pyspark.py)
- [orders_data_clean.parquet](orders_data_clean.parquet)

---

## 📋 Example Output (After Running Script)

| order_date | order_id | product                  | category     | purchase_state | quantity_ordered | price_each | turnover | margin | time_of_day |
| ---------- | -------- | ------------------------ | ------------ | -------------- | ---------------- | ---------- | -------- | ------ | ----------- |
| 2023-01-22 | 141234   | iphone                   | vêtements    | MA             | 1                | 700.00     | 700.00   | 469.00 | evening     |
| 2023-01-28 | 141235   | lightning charging cable | alimentation | OR             | 1                | 14.95      | 14.95    | 7.48   | afternoon   |
| 2023-01-17 | 141236   | wired headphones         | vêtements    | CA             | 2                | 11.99      | 23.98    | 11.99  | afternoon   |
| 2023-01-05 | 141237   | 27in fhd monitor         | sports       | CA             | 1                | 149.99     | 149.99   | 52.50  | evening     |
| 2023-01-25 | 141238   | wired headphones         | électronique | TX             | 1                | 11.99      | 11.99    | 5.99   | morning     |

---

## 👨‍💻 Learning Source

This project was developed as part of the **DataCamp Data Engineering curriculum**, focusing on real-world PySpark data cleaning pipelines.

---

⭐ **If you found this project useful, check out more of my projects on GitHub!**
