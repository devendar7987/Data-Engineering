# 🚇 Project: Exploring London's Travel Network

## 📂 Location

`SQL/Exploring London's Travel Network/`

## 👨‍💻 Author

**Devendar Thigulla**  
📅 _Created on_: 2025‑08‑06

---

## ✨ Overview

This project uses SQL to analyze Transport for London (TfL) journey data and answer real-world questions about public transport usage in London.

TfL operates transport services across London including the **Underground & DLR**, **Buses**, **Trams**, **Overground**, **Emirates Airline**, and **TfL Rail**. With over 8.5 million residents and 300+ spoken languages, London relies heavily on efficient public transport.

Using a dataset containing millions of journeys across transport types and dates, we answer three key business questions using SQL in Snowflake.

---

## 📄 Dataset: `TFL.JOURNEYS`

### Journey Types in Dataset:

The dataset contains public transport usage data for the following modes:

- 🚇 Underground & DLR
- 🚌 Bus
- 🚋 Tram
- 🚆 Overground
- 🚡 Emirates Airline
- 🚈 TfL Rail

| Column Name         | Description                                      | Data Type |
| ------------------- | ------------------------------------------------ | --------- |
| `MONTH`             | Month number (e.g., 1 = January)                 | INTEGER   |
| `YEAR`              | Year of journey data                             | INTEGER   |
| `DAYS`              | Number of days in the month                      | INTEGER   |
| `REPORT_DATE`       | Date when the data was officially reported       | DATE      |
| `JOURNEY_TYPE`      | Type of transport (e.g., Bus, Underground & DLR) | VARCHAR   |
| `JOURNEYS_MILLIONS` | Number of journeys made, in millions (decimal)   | FLOAT     |

---

## 🎯 Objectives

You will write 3 SQL queries to answer the following:

### 1. **Most Popular Transport Types**

- ✅ Calculate the total number of journeys for each transport type.
- ✅ Return columns: `JOURNEY_TYPE`, `TOTAL_JOURNEYS_MILLIONS`.
- ✅ Sort by journey volume (descending).
- ✅ **Saved as**: `most_popular_transport_types`

---

### 2. **Top 5 Months for Emirates Airline**

- ✅ Filter to only `JOURNEY_TYPE = 'Emirates Airline'`
- ✅ Exclude rows where `JOURNEYS_MILLIONS` is NULL.
- ✅ Round journey values to 2 decimal places.
- ✅ Return columns: `MONTH`, `YEAR`, `ROUNDED_JOURNEYS_MILLIONS`.
- ✅ Sort by journey volume (descending).
- ✅ **Saved as**: `emirates_airline_popularity`

---

### 3. **Least Popular Years for Underground & DLR**

- ✅ Filter to only `JOURNEY_TYPE = 'Underground & DLR'`
- ✅ Group by year and sum journeys.
- ✅ Return: `YEAR`, `JOURNEY_TYPE`, `TOTAL_JOURNEYS_MILLIONS`.
- ✅ Sort by journey volume (ascending).
- ✅ **Saved as**: `least_popular_years_tube`

---

## 🛠️ SQL Concepts Used

- `GROUP BY` with `SUM()` and `ROUND()`
- `ORDER BY` with `DESC` and `ASC`
- Filtering with `WHERE` and `IS NOT NULL`
- `LIMIT` to return top/bottom results
- Aliasing columns for clarity

---

📜 **Query Files & Result Datasets**  
This project includes three SQL queries and their corresponding output files:

- [most_popular_transport_types.sql](most_popular_transport_types.sql) → [most_popular_transport_types.csv](most_popular_transport_types.csv)
- [emirates_airline_popularity.sql](emirates_airline_popularity.sql) → [emirates_airline_popularity.csv](emirates_airline_popularity.csv)
- [least_popular_years_tube.sql](least_popular_years_tube.sql) → [least_popular_years_tube.csv](least_popular_years_tube.csv)

---

## 📋 Example Outputs

### most_popular_transport_types

| JOURNEY_TYPE      | TOTAL_JOURNEYS_MILLIONS |
| ----------------- | ----------------------- |
| London Bus        | 4000.00                 |
| Underground & DLR | 3600.45                 |
| ...               | ...                     |

### emirates_airline_popularity

| MONTH | YEAR | ROUNDED_JOURNEYS_MILLIONS |
| ----- | ---- | ------------------------- |
| 7     | 2016 | 0.23                      |
| 8     | 2015 | 0.21                      |
| ...   | ...  | ...                       |

### least_popular_years_tube

| YEAR | JOURNEY_TYPE      | TOTAL_JOURNEYS_MILLIONS |
| ---- | ----------------- | ----------------------- |
| 2020 | Underground & DLR | 645.00                  |
| 2021 | Underground & DLR | 670.00                  |
| ...  | ...               | ...                     |

---

## 👨‍💻 Learning Source

This project was completed as part of my learning through **DataCamp**, using Snowflake SQL to analyze public transportation usage in London.

---

⭐ **If you found this project useful, feel free to explore more in my GitHub repositories!**
