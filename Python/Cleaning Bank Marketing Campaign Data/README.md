# 🏦 Project: Cleaning Bank Marketing Campaign Data

## 📂 Location

`Python/Cleaning Bank Marketing Campaign Data/`

## 👨‍💻 Author

**Devendar Thigulla**
📅 _Created on_: 2025-09-09

---

## ✨ Overview

This project uses **Python (Pandas \& NumPy)** to clean and reformat the `bank_marketing.csv` dataset, which was collected during a recent marketing campaign by a bank promoting **personal loans**.

Personal loans are a major revenue stream for banks. For example, in September 2022, UK consumers borrowed **£1.5 billion in loans**. At an average interest rate of ~10% for two years, banks could earn **~£300 million in interest**.

To prepare for future campaigns, the bank requested a **clean, structured dataset** that can be easily loaded into a **PostgreSQL database**. This ensures consistent formatting and allows new campaign data to be added seamlessly.

The project focuses on:

- Subsetting, cleaning, and transforming the raw data
- Splitting into **three structured datasets**: `client`, `campaign`, and `economics`
- Exporting cleaned results to **CSV files**

---

## 📄 Dataset: `bank_marketing.csv`

The original dataset contains information about **clients**, **campaign details**, and **economic indicators**.

The final cleaned datasets are split into **three parts**:

---

### 1. `client.csv`

| Column         | Data Type | Description                      | Cleaning Applied                      |
| :------------- | :-------- | :------------------------------- | :------------------------------------ |
| client_id      | INTEGER   | Client ID                        | N/A                                   |
| age            | INTEGER   | Client's age                     | N/A                                   |
| job            | OBJECT    | Client's job                     | Replace `.` with `_`                  |
| marital        | OBJECT    | Marital status                   | N/A                                   |
| education      | OBJECT    | Education level                  | Replace `.` with `_`, `unknown` → NaN |
| credit_default | BOOL      | Credit in default                | `"yes"` → True, else False            |
| mortgage       | BOOL      | Existing mortgage (housing loan) | `"yes"` → True, else False            |

---

### 2. `campaign.csv`

| Column                     | Data Type | Description                          | Cleaning Applied                    |
| :------------------------- | :-------- | :----------------------------------- | :---------------------------------- |
| client_id                  | INTEGER   | Client ID                            | N/A                                 |
| number_contacts            | INTEGER   | Contacts in campaign                 | N/A                                 |
| contact_duration           | INTEGER   | Last contact duration (secs)         | N/A                                 |
| previous_campaign_contacts | INTEGER   | Previous campaign contacts           | N/A                                 |
| previous_outcome           | BOOL      | Previous campaign outcome            | `"success"` → True, else False      |
| campaign_outcome           | BOOL      | Current campaign outcome             | `"yes"` → True, else False          |
| last_contact_date          | DATETIME  | Last contact date (YYYY-MM-DD, 2022) | Built from day + month + fixed year |

---

### 3. `economics.csv`

| Column               | Data Type | Description                        | Cleaning Applied |
| :------------------- | :-------- | :--------------------------------- | :--------------- |
| client_id            | INTEGER   | Client ID                          | N/A              |
| cons_price_idx       | FLOAT     | Consumer price index (monthly)     | N/A              |
| euribor_three_months | FLOAT     | Euro Interbank Offered Rate (3-mo) | N/A              |

---

## 🎯 Objectives

- Subset \& split data into **client**, **campaign**, and **economics**
- Clean \& transform fields according to **bank specifications**
- Handle missing values and ensure consistent formatting
- Export results as **clean CSV files**

---

## 🛠️ Tools \& Techniques

- **Python** → Data cleaning \& transformation
- **Pandas** → Subsetting, formatting, column transformations
- **NumPy** → Handling missing values (`np.NaN`)
- **Datetime conversion** → Building `last_contact_date`

**Key operations included:**

- **String replacements** (`"." → "_"`)
- **Boolean conversion** (`yes/no`, `success/failure`)
- **Handling missing values** (`unknown → NaN`)
- **Constructing proper dates** with `pd.to_datetime()`

---

## 📜 Script \& Result Datasets

This project includes a single Python script and its corresponding cleaned output files:

- [cleaning_bank_marketing_campaign_data.py](cleaning_bank_marketing_campaign_data.py)
- [client.csv](client.csv)
- [campaign.csv](campaign.csv)
- [economics.csv](economics.csv)

---

## 📋 Example Outputs

### client.csv

```
client_id   age   job         marital   education     credit_default   mortgage
----------- ----- ----------- --------- ------------- ---------------- ----------

0           56    housemaid   married   basic_4y      False            False
1           57    services    married   high_school   False            False
2           37    services    married   high_school   False            True
```

### campaign.csv

```
client_id   number_contacts   contact_duration   previous_campaign_contacts   previous_outcome   campaign_outcome   last_contact_date
----------- ----------------- ------------------ ---------------------------- ------------------ ------------------ -------------------

0           1                 261                0                            False              False              2022-05-13
1           1                 149                0                            False              False              2022-05-19
2           1                 226                0                            False              False              2022-05-23
```

### economics.csv

```
client_id   cons_price_idx   euribor_three_months
----------- ---------------- ----------------------

0           93.994           4.857
1           93.994           4.857
2           93.994           4.857
```

---

## 👨‍💻 Learning Source

This project was completed as part of my **Data Cleaning practice with Pandas**. The workflow simulates real-world requirements where banks need structured, clean, and **database-ready data** for campaign analysis.

---

⭐ **If you found this project useful, check out more of my projects on GitHub!**
