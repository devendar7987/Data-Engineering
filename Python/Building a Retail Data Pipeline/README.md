# 🏬 Project: Building a Retail Data Pipeline

## 📂 Location

`Python/Building a Retail Data Pipeline/`

## 👨‍💻 Author

**Devendar Thigulla**  
📅 _Created on_: 2025-10-25

---

## ✨ Overview

This project uses **Python (Pandas)** to build and automate a **data pipeline** for analyzing **Walmart’s e-commerce sales** during major holidays such as the **Super Bowl, Labour Day, Thanksgiving, and Christmas**.

By the end of 2022, Walmart’s online sales reached **$80 billion**, accounting for **13% of total company revenue**. This analysis helps understand how holiday seasons affect sales performance, supporting better **inventory and supply chain planning**.

The project focuses on:

- Extracting data from multiple sources
- Cleaning and transforming it into a structured format
- Aggregating monthly sales for trend analysis
- Validating the output CSV files to ensure successful data export

---

## 📄 Datasets

The project uses **two main data sources** representing Walmart’s retail sales and supplementary information.

### 1. `grocery_sales` (PostgreSQL Table)

| Column       | Description                   |
| :----------- | :---------------------------- |
| index        | Unique row ID                 |
| Store_ID     | Store identifier number       |
| Date         | Week of sales (YYYY-MM-DD)    |
| Weekly_Sales | Weekly sales amount per store |

### 2. `extra_data.parquet`

| Column       | Description                             |
| :----------- | :-------------------------------------- |
| IsHoliday    | 1 if the week contains a public holiday |
| Temperature  | Temperature during the sales week       |
| Fuel_Price   | Regional fuel price                     |
| CPI          | Consumer Price Index                    |
| Unemployment | Regional unemployment rate              |
| MarkDown1–4  | Promotional markdowns                   |
| Dept         | Department number in the store          |
| Size         | Store size                              |
| Type         | Store type (based on size)              |

---

## 🎯 Objectives

- Merge and clean Walmart’s sales and external datasets
- Handle missing and inconsistent values
- Extract **month** information for time-based analysis
- Compute **average monthly sales** using aggregation
- Export cleaned and aggregated datasets as **CSV files**
- Verify that the exported CSV files were created correctly

---

## 🧩 Process Overview

### 1. **Extract**

Merges `grocery_sales` and `extra_data.parquet` using the common key `index`.

### 2. **Transform**

- Fills missing numerical fields (`CPI`, `Weekly_Sales`, `Unemployment`)
- Converts `Date` to datetime format and extracts `Month`
- Filters rows where `Weekly_Sales` > 10,000
- Drops unnecessary columns

**Result DataFrame:** `clean_df`

### 3. **Aggregate**

- Groups data by `Month` and calculates **average Weekly_Sales**
- Rounds results to two decimal places

**Result DataFrame:** `agg_df`

### 4. **Load**

Converts `clean_df` → `clean_data.csv` and `agg_df` → `agg_data.csv`, both saved without index values.

### 5. **Validation**

Checks for the existence of output CSV files in the working directory after loading.

---

## 🛠️ Tools & Techniques

- **Python (3.13+)** → Data processing and automation
- **Pandas** → Cleaning, transformation, and aggregation
- **os** → File verification and management
- **Datetime processing** → Extracting months from `Date` columns

**Key operations included:**

- Filling missing values (`CPI`, `Weekly_Sales`, `Unemployment`)
- Datetime conversion (`pd.to_datetime`)
- Filtering invalid records (`Weekly_Sales` > 10,000)
- Grouping and averaging for trend insights

---

## 📜 Script & Result Datasets

This project includes one Python script and its corresponding outputs:

- [walmart_data_pipeline.py](walmart_data_pipeline.py)
- [clean_data.csv](clean_data.csv)
- [agg_data.csv](agg_data.csv)

---

## 📋 Example Outputs

### clean_data.csv

| Column       | Description                          |
| :----------- | :----------------------------------- |
| Store_ID     | Store identifier                     |
| Month        | Month extracted from Date (1–12)     |
| Dept         | Department number                    |
| IsHoliday    | Indicates if week includes a holiday |
| Weekly_Sales | Weekly sales amount                  |
| CPI          | Consumer Price Index                 |
| Unemployment | Unemployment rate                    |

### agg_data.csv

| Column    | Description                    |
| :-------- | :----------------------------- |
| Month     | Month number (1–12)            |
| Avg_Sales | Average weekly sales per month |

---

## 👨‍💻 Learning Source

This project was developed as part of the **DataCamp Data Engineering curriculum**, focusing on **end-to-end data pipeline design** for Walmart’s e-commerce sales analysis using **Python and Pandas**.

---

⭐ **If you found this project useful, check out more of my projects on GitHub!**
