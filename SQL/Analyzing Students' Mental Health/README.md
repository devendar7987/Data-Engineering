# 📌 Project: Analyzing Students' Mental Health 🌈

## 📂 Location
`SQL/Analyzing-Students-Mental-Health/`

## 👨‍💻 Author
**Devendar Thigulla**  
📅 *Created on*: 2025‑07‑24

---

## ✨ Overview
This project explores whether the **length of stay (`stay`)** impacts the average mental health scores of international students at a Japanese university.  

The analysis uses SQL to group students by their stay length and calculate average mental health indicators.

---

## 📄 Dataset: `students`

| Column Name   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `inter_dom`   | Type of student: `Inter` (International) or `Dom` (Domestic)               |
| `stay`        | Length of stay in years                                                    |
| `todep`       | Total depression score (PHQ‑9)                                             |
| `tosc`        | Total social connectedness score (SCS)                                     |
| `toas`        | Total acculturative stress score (ASISS)                                   |
| `japanese_cate` | Japanese language proficiency category                                   |
| `english_cate`  | English language proficiency category                                    |
| `academic`    | Current academic level (Undergraduate / Graduate)                          |
| `age`         | Current age of student                                                     |

---

## 🎯 Objective
✅ Focus only on international students (`inter_dom = 'Inter'`).  
✅ Group them by `stay` (years of stay).  
✅ For each group, calculate:
- **`count_int`** → number of international students
- **`average_phq`** → average PHQ‑9 score (depression)
- **`average_scs`** → average SCS score (social connectedness)
- **`average_as`** → average ASISS score (acculturative stress)

✅ Sort the result by stay (descending).  
✅ Return only the top 9 stay groups.

---

## 🛠️ SQL Concepts Used
- `GROUP BY` with aggregation (`COUNT`, `AVG`)
- `ROUND()` for formatting averages
- Filtering with `WHERE`
- Sorting with `ORDER BY`
- Limiting with `LIMIT`

---

## 📜 Main Query
See [Analyzing-Students-Mental-Health.sql](Analyzing-Students-Mental-Health.sql) for the complete SQL code.

---

## 📋 Example Result

| stay | count_int | average_phq | average_scs | average_as |
|------|-----------|-------------|-------------|------------|
| 10   | 1         | 13.00       | 32.00       | 50.00      |
| 8    | 1         | 10.00       | 44.00       | 65.00      |
| 7    | 1         | 4.00        | 48.00       | 45.00      |
| …    | …         | …           | …           | …          |


---

## 👨‍💻 Learning Source
This project was built as part of my learning journey through **DataCamp** and documented here to showcase my growing skills in **Data Engineering**.

---
⭐ **If you like this project, please consider giving my repository a star!**
