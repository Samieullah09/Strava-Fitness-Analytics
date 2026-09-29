# 🏃 Strava Fitness Analytics

A Streamlit + SQL analytics app built on the Fitbit fitness tracker dataset
(33 users, 12 Apr – 12 May 2016). Includes a full interactive dashboard and
a SQL Playground with 30 predefined analytical questions.

\---

## 📋 Business Task

Analyze how users engage with their fitness tracker (steps, calories, sleep,
heart rate, and weight) to uncover activity patterns and provide
data-driven recommendations for improving user engagement.

\---

## 🗂️ App Structure

|File / Page|What it does|
|-|-|
|`Home.py`|Landing page — KPI overview, business task, navigation guide, and collapsible sections for Data Description, Limitations, and Future Work|
|`pages/1\_Dashboard.py`|10-tab dashboard (Overview, Daily Activity, Calories, Intensity, Distance, Hourly, Sleep, Heart Rate, Weight/BMI, Leaderboard) with an All Users / individual user filter|
|`pages/2\_SQL\_Playground.py`|30 predefined SQL questions — pick one from the dropdown, view the SQL behind it, run it, and see the result as a table + auto-generated chart|
|`build\_db.py`|One-time script that builds `fitbit.db` from the raw CSVs|
|`queries.py`|All 30 SQL questions as a lookup dictionary, plus a dynamic leaderboard query builder|
|`user\_labels.py`|Maps anonymized numeric Fitbit Ids to friendly `User 1, User 2...` display labels|
|`theme.py`|Shared sports/digital visual theme (dark background image, Strava-orange accents, sidebar branding, logo) applied across every page|

\---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python build\_db.py        # builds fitbit.db from the raw CSVs (run once)
streamlit run Home.py
```

The app opens with three pages in the sidebar: **Home**, **Dashboard**, and
**SQL Playground**.

\---

## 🗃️ Data Sources

The raw dataset has 18 CSV files. Several are duplicates or subsets of each
other, so not all 18 were loaded — here's the decision made on each:

|#|File|Decision|Reason|
|-|-|-|-|
|1|dailyActivity\_merged|✅ Used|Core daily table|
|2|dailyCalories\_merged|❌ Skipped|Already included in dailyActivity|
|3|dailyIntensities\_merged|❌ Skipped|Already included in dailyActivity|
|4|dailySteps\_merged|❌ Skipped|Already included in dailyActivity|
|5|sleepDay\_merged|✅ Used|Sleep table|
|6|weightLogInfo\_merged|✅ Used|Weight/BMI table|
|7|hourlySteps\_merged|✅ Used|Hourly pattern analysis|
|8|hourlyCalories\_merged|✅ Used|Hourly pattern analysis|
|9|hourlyIntensities\_merged|✅ Used|Hourly pattern analysis|
|10|heartrate\_seconds\_merged|✅ Used (aggregated)|2.48M raw rows → aggregated to per-user-per-hour average|
|11|minuteCaloriesNarrow\_merged|❌ Skipped|Covered by hourlyCalories|
|12|minuteCaloriesWide\_merged|❌ Skipped|Duplicate of Narrow, different shape|
|13|minuteIntensitiesNarrow\_merged|❌ Skipped|Covered by hourlyIntensities|
|14|minuteIntensitiesWide\_merged|❌ Skipped|Duplicate of Narrow, different shape|
|15|minuteStepsNarrow\_merged|❌ Skipped|Covered by hourlySteps|
|16|minuteStepsWide\_merged|❌ Skipped|Duplicate of Narrow, different shape|
|17|minuteMETsNarrow\_merged|✅ Used (aggregated)|New metric not covered elsewhere; 1.3M raw rows → aggregated to per-user-per-day average|
|18|minuteSleep\_merged|❌ Skipped|sleepDay already gives the daily summary needed|

\---

## 🧹 Data Cleaning

* Duplicate rows dropped from every table
* Date/time columns parsed to proper datetime types
* Heart rate (2.48M rows) and METs (1.3M rows) pre-aggregated before loading,
since raw minute/second-level data is too heavy for dashboard queries
* Data quality checks: 79 rows found where `SedentaryMinutes = 1440` (tracker
not worn that day); 3 users have fewer than 20 tracked days out of 31

\---

## 🆔 User Identification

The dataset has no real names — only anonymized numeric Ids (privacy-protected,
collected via Amazon Mechanical Turk). The app maps each Id to a friendly
`User 1`, `User 2`, ... label (sorted by Id) for readability, while keeping
the original Id visible alongside it in the SQL Playground results.

\---

## 📊 Dashboard Sections

Overview • Daily Activity • Calories • Intensity • Distance • Hourly •
Sleep • Heart Rate • Weight/BMI • Leaderboard (Top/Bottom 10 by any metric,
always shown across all users regardless of the sidebar filter).

## 🛢️ SQL Playground

30 fixed, dropdown-selectable SQL questions spanning overview stats, trends,
correlations, hourly patterns, sleep analysis, and advanced SQL (`RANK()`
window function, 7-day rolling average). Each question shows its SQL query,
a results table, and an auto-generated chart where appropriate.

\---

## ⚠️ Limitations

* Only 33 users and 1 month of data — results may not generalize to a wider population
* No demographic info (age, sex, profession) — can't segment by these
* Weight data covers very few users — BMI insights are not statistically strong
* Not every user has a full 31 days tracked

## 🚀 Future Work

* Connect to a live fitness-tracker API instead of a static CSV export
* Schedule a daily job to refresh the database automatically
* Monitor for data drift (e.g. sudden drop in active users) and alert if detected
* Expand to a larger, more demographically diverse user base

\---

## 🛠️ Tech Stack

Python • Streamlit • SQLite • Pandas • Plotly

