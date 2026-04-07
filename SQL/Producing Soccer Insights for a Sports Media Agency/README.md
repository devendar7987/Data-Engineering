# ⚽ Project: Producing Soccer Insights for a Sports Media Agency

## 📂 Location

`SQL/Producing Soccer Insights for a Sports Media Agency/`

---

## 👨‍💻 Author

**Devendar Thigulla**  
📅 _Created on_: 2026-04-06

---

## ✨ Overview

This project uses SQL in Snowflake to analyze match data from the UEFA Champions League across multiple seasons.

The UEFA Champions League is one of the most prestigious football tournaments in the world, featuring top European clubs competing at the highest level. The dataset captures detailed match-level statistics such as goals, possession, duels won, and match predictions.

Using structured data from three seasons, this project answers key analytical questions to uncover team performance, dominance patterns, and unexpected match outcomes.

---

## 📄 Schema: `SOCCER`

### Tables Used:

- `TBL_UEFA_2020`
- `TBL_UEFA_2021`
- `TBL_UEFA_2022`

---

## 📊 Key Columns in Tables:

| Column Name                   | Description                                              | Data Type    |
|------------------------------|----------------------------------------------------------|-------------|
| `STAGE`                      | Stage of the match                                       | VARCHAR(50) |
| `DATE`                       | Date when the match occurred                             | DATE        |
| `PENS`                       | Indicates if the match ended in penalties                | VARCHAR(50) |
| `PENS_HOME_SCORE`            | Penalty score by home team                               | VARCHAR(50) |
| `PENS_AWAY_SCORE`            | Penalty score by away team                               | VARCHAR(50) |
| `TEAM_NAME_HOME`             | Home team name                                           | VARCHAR(50) |
| `TEAM_NAME_AWAY`             | Away team name                                           | VARCHAR(50) |
| `TEAM_HOME_SCORE`            | Goals scored by home team                                | NUMBER      |
| `TEAM_AWAY_SCORE`            | Goals scored by away team                                | NUMBER      |
| `POSSESSION_HOME`            | Ball possession percentage of home team                  | FLOAT       |
| `POSSESSION_AWAY`            | Ball possession percentage of away team                  | FLOAT       |
| `TOTAL_SHOTS_HOME`           | Total shots taken by home team                           | NUMBER      |
| `TOTAL_SHOTS_AWAY`           | Total shots taken by away team                           | NUMBER      |
| `SHOTS_ON_TARGET_HOME`       | Shots on target by home team                             | FLOAT       |
| `SHOTS_ON_TARGET_AWAY`       | Shots on target by away team                             | FLOAT       |
| `DUELS_WON_HOME`             | Duels won by home team                                   | NUMBER      |
| `DUELS_WON_AWAY`             | Duels won by away team                                   | NUMBER      |
| `PREDICTION_TEAM_HOME_WIN`   | Probability of home team winning                         | FLOAT       |
| `PREDICTION_DRAW`            | Probability of draw                                      | FLOAT       |
| `PREDICTION_TEAM_AWAY_WIN`   | Probability of away team winning                         | FLOAT       |
| `LOCATION`                   | Stadium where the match was held                         | VARCHAR(50) |

---

## 🎯 Objectives

You will write 3 SQL queries to answer the following:

### 1. **Top 3 Home Teams by Goals (2020–21)**

- ✅ Identify teams with highest home goals  
- ✅ Return: `TEAM_NAME_HOME`, `TEAM_HOME_SCORE`  
- ✅ Sort by goals (descending)  
- ✅ **Saved as**: `TEAM_HOME_WITH_MOST_GOALS`

---

### 2. **Team with Maximum Possession Dominance (2021–22)**

- ✅ Find team with majority possession in most matches  
- ✅ Return: `TEAM_NAME`, `GAME_COUNT`  
- ✅ Sort by game count (descending)  
- ✅ **Saved as**: `TEAM_WITH_MAJORITY_POSSESSION`

---

### 3. **Teams That Won Duels but Lost Matches (2022–23)**

- ✅ Identify teams that won duels but still lost  
- ✅ Return: `STAGE`, `TEAM_LOST`  
- ✅ Filter only valid cases  
- ✅ **Saved as**: `TEAM_WON_DUEL_LOST_GAME_STAGE_WISE`

---

## 🛠️ SQL Concepts Used

- `CASE` statements for conditional logic  
- `GROUP BY` with aggregation (`COUNT`)  
- Filtering using `WHERE`  
- Sorting with `ORDER BY`  
- Limiting results using `LIMIT`  

---

## 📜 Query Files & Result Datasets  

### 🔹 Query Files

- [team_home_with_most_goals.sql](./queries/team_home_with_most_goals.sql)  
- [team_with_majority_possession.sql](./queries/team_with_majority_possession.sql)  
- [team_won_duel_lost_game_stage_wise.sql](./queries/team_won_duel_lost_game_stage_wise.sql)  

---

### 🔹 Result Files (CSV Outputs)

- [team_home_with_most_goals.csv](./results/team_home_with_most_goals.csv)  
- [team_with_majority_possession.csv](./results/team_with_majority_possession.csv)  
- [team_won_duel_lost_game_stage_wise.csv](./results/team_won_duel_lost_game_stage_wise.csv)  

---

## 📋 Example Outputs

### team_home_with_most_goals

| TEAM_NAME_HOME     | TEAM_HOME_SCORE |
|-------------------|----------------|
| PSG               | 5              |
| Manchester United | 5              |
| Barcelona         | 5              |

---

### team_with_majority_possession

| TEAM_NAME | GAME_COUNT |
|-----------|------------|
| Liverpool | 9          |

---

### team_won_duel_lost_game_stage_wise

| STAGE                   | TEAM_LOST         |
|------------------------|-------------------|
| Group stage: Matchday 1 | Chelsea           |
| Group stage: Matchday 1 | København         |
| Group stage: Matchday 1 | Juventus          |
| Group stage: Matchday 1 | Maccabi Haifa     |
| Group stage: Matchday 1 | Rangers           |
| Group stage: Matchday 1 | Liverpool         |
| Group stage: Matchday 1 | Porto             |
| Group stage: Matchday 1 | Bayer Leverkusen  |

---

## 👨‍💻 Learning Source

This project was completed as part of my learning through **DataCamp**, focusing on Snowflake SQL for real-world sports data analysis.

---

⭐ **If you found this project useful, feel free to explore more in my GitHub repositories!**
