"""
All 30 predefined SQL questions for the SQL Playground page.
"""

QUERIES = {

    # ---------- Section 1: Overview ----------
    "1. How many unique users are in the dataset?": """
        SELECT COUNT(DISTINCT Id) AS total_users FROM daily_activity;
    """,

    "2. What is the average daily steps (overall)?": """
        SELECT ROUND(AVG(TotalSteps), 0) AS avg_daily_steps FROM daily_activity;
    """,

    "3. What is the average daily calories burned?": """
        SELECT ROUND(AVG(Calories), 0) AS avg_daily_calories FROM daily_activity;
    """,

    "4. What is the average daily distance covered?": """
        SELECT ROUND(AVG(TotalDistance), 2) AS avg_daily_distance FROM daily_activity;
    """,

    "5. What % of tracked time is Sedentary vs Active?": """
        SELECT
            ROUND(100.0 * SUM(SedentaryMinutes) /
                SUM(SedentaryMinutes + LightlyActiveMinutes + FairlyActiveMinutes + VeryActiveMinutes), 1)
                AS sedentary_pct,
            ROUND(100.0 * SUM(LightlyActiveMinutes + FairlyActiveMinutes + VeryActiveMinutes) /
                SUM(SedentaryMinutes + LightlyActiveMinutes + FairlyActiveMinutes + VeryActiveMinutes), 1)
                AS active_pct
        FROM daily_activity;
    """,

    # ---------- Section 2: Daily Activity ----------
    "6. How does daily step count trend over time?": """
        SELECT ActivityDate, ROUND(AVG(TotalSteps), 0) AS avg_steps
        FROM daily_activity
        GROUP BY ActivityDate
        ORDER BY ActivityDate;
    """,

    "7. Which weekday has the highest average steps?": """
        SELECT strftime('%w', ActivityDate) AS weekday, ROUND(AVG(TotalSteps), 0) AS avg_steps
        FROM daily_activity
        GROUP BY weekday
        ORDER BY avg_steps DESC;
    """,

    "8. Which weekday has the lowest average steps?": """
        SELECT strftime('%w', ActivityDate) AS weekday, ROUND(AVG(TotalSteps), 0) AS avg_steps
        FROM daily_activity
        GROUP BY weekday
        ORDER BY avg_steps ASC;
    """,

    # ---------- Section 3: Calories ----------
    "9. How does daily calorie burn trend over time?": """
        SELECT ActivityDate, ROUND(AVG(Calories), 0) AS avg_calories
        FROM daily_activity
        GROUP BY ActivityDate
        ORDER BY ActivityDate;
    """,

    "10. Is there a correlation between steps and calories?": """
        SELECT TotalSteps, Calories FROM daily_activity;
    """,

    "11. Which users burn high calories but take relatively few steps?": """
        SELECT Id,
               ROUND(AVG(TotalSteps), 0) AS avg_steps,
               ROUND(AVG(Calories), 0) AS avg_calories
        FROM daily_activity
        GROUP BY Id
        HAVING avg_calories > (SELECT AVG(Calories) FROM daily_activity)
           AND avg_steps < (SELECT AVG(TotalSteps) FROM daily_activity)
        ORDER BY avg_calories DESC;
    """,

    # ---------- Section 4: Intensity ----------
    "12. How is activity time distributed across intensity levels?": """
        SELECT
            ROUND(AVG(SedentaryMinutes), 0) AS avg_sedentary,
            ROUND(AVG(LightlyActiveMinutes), 0) AS avg_light,
            ROUND(AVG(FairlyActiveMinutes), 0) AS avg_fair,
            ROUND(AVG(VeryActiveMinutes), 0) AS avg_very_active
        FROM daily_activity;
    """,

    "13. What % of the day is spent in each intensity level?": """
        SELECT
            ROUND(100.0 * SUM(SedentaryMinutes) / SUM(SedentaryMinutes+LightlyActiveMinutes+FairlyActiveMinutes+VeryActiveMinutes), 1) AS sedentary_pct,
            ROUND(100.0 * SUM(LightlyActiveMinutes) / SUM(SedentaryMinutes+LightlyActiveMinutes+FairlyActiveMinutes+VeryActiveMinutes), 1) AS light_pct,
            ROUND(100.0 * SUM(FairlyActiveMinutes) / SUM(SedentaryMinutes+LightlyActiveMinutes+FairlyActiveMinutes+VeryActiveMinutes), 1) AS fair_pct,
            ROUND(100.0 * SUM(VeryActiveMinutes) / SUM(SedentaryMinutes+LightlyActiveMinutes+FairlyActiveMinutes+VeryActiveMinutes), 1) AS very_active_pct
        FROM daily_activity;
    """,

    "14. Which weekday has the highest Very-Active minutes?": """
        SELECT strftime('%w', ActivityDate) AS weekday, ROUND(AVG(VeryActiveMinutes), 1) AS avg_very_active
        FROM daily_activity
        GROUP BY weekday
        ORDER BY avg_very_active DESC;
    """,

    "15. How does Sedentary time compare with Active time?": """
        SELECT
            ROUND(AVG(SedentaryMinutes), 0) AS avg_sedentary,
            ROUND(AVG(LightlyActiveMinutes + FairlyActiveMinutes + VeryActiveMinutes), 0) AS avg_active
        FROM daily_activity;
    """,

    # ---------- Section 5: Distance ----------
    "16. How does daily distance trend over time?": """
        SELECT ActivityDate, ROUND(AVG(TotalDistance), 2) AS avg_distance
        FROM daily_activity
        GROUP BY ActivityDate
        ORDER BY ActivityDate;
    """,

    "17. What is the relationship between steps and distance?": """
        SELECT TotalSteps, TotalDistance FROM daily_activity;
    """,

    # ---------- Section 6: Hourly ----------
    "18. At what hour are the most steps taken?": """
        SELECT strftime('%H', ActivityHour) AS hour_of_day, ROUND(AVG(StepTotal), 0) AS avg_steps
        FROM hourly_steps
        GROUP BY hour_of_day
        ORDER BY avg_steps DESC;
    """,

    "19. At what hour are the most calories burned?": """
        SELECT strftime('%H', ActivityHour) AS hour_of_day, ROUND(AVG(Calories), 1) AS avg_calories
        FROM hourly_calories
        GROUP BY hour_of_day
        ORDER BY avg_calories DESC;
    """,

    "20. How does activity differ across Morning/Afternoon/Evening/Night?": """
        SELECT
            CASE
                WHEN CAST(strftime('%H', ActivityHour) AS INTEGER) BETWEEN 5 AND 11 THEN 'Morning'
                WHEN CAST(strftime('%H', ActivityHour) AS INTEGER) BETWEEN 12 AND 16 THEN 'Afternoon'
                WHEN CAST(strftime('%H', ActivityHour) AS INTEGER) BETWEEN 17 AND 20 THEN 'Evening'
                ELSE 'Night'
            END AS part_of_day,
            ROUND(AVG(StepTotal), 0) AS avg_steps
        FROM hourly_steps
        GROUP BY part_of_day
        ORDER BY avg_steps DESC;
    """,

    # ---------- Section 7: Sleep ----------
    "21. What is the average sleep duration?": """
        SELECT ROUND(AVG(TotalMinutesAsleep), 0) AS avg_sleep_minutes FROM sleep_day;
    """,

    "22. How does sleep duration vary by weekday?": """
        SELECT strftime('%w', SleepDay) AS weekday, ROUND(AVG(TotalMinutesAsleep), 0) AS avg_sleep_minutes
        FROM sleep_day
        GROUP BY weekday
        ORDER BY avg_sleep_minutes DESC;
    """,

    "23. What is the relationship between sleep duration and daily steps?": """
        SELECT s.TotalMinutesAsleep, d.TotalSteps
        FROM sleep_day s
        JOIN daily_activity d
            ON s.Id = d.Id AND DATE(s.SleepDay) = DATE(d.ActivityDate);
    """,

    "24. What is the gap between time in bed and actual sleep?": """
        SELECT ROUND(AVG(TotalTimeInBed - TotalMinutesAsleep), 0) AS avg_awake_minutes_in_bed
        FROM sleep_day;
    """,

    # ---------- Section 8: Heart Rate ----------
    "25. What is the average heart rate, and at what hour does it peak?": """
        SELECT strftime('%H', ActivityHour) AS hour_of_day, ROUND(AVG(AvgHeartRate), 1) AS avg_heart_rate
        FROM heart_rate_hourly
        GROUP BY hour_of_day
        ORDER BY avg_heart_rate DESC;
    """,

    # ---------- Section 9: Weight / BMI ----------
    "26. What is the average BMI of users with weight records?": """
        SELECT ROUND(AVG(BMI), 1) AS avg_bmi FROM weight_log;
    """,

    "27. How does weight trend over the tracking period?": """
        SELECT Date, WeightKg FROM weight_log ORDER BY Date;
    """,

    # ---------- Section 10: Leaderboard (built dynamically, see function below) ----------
    "28. Leaderboard: Top/Bottom 10 users by a chosen metric": """
        -- Built dynamically in the Streamlit app based on the metric dropdown.
        -- See build_leaderboard_query() below.
    """,

    # ---------- Section 11: Advanced SQL ----------
    "29. Rank users by average daily steps": """
        SELECT Id, ROUND(AVG(TotalSteps), 0) AS avg_steps,
               RANK() OVER (ORDER BY AVG(TotalSteps) DESC) AS steps_rank
        FROM daily_activity
        GROUP BY Id;
    """,

    "30. 7-day rolling average of steps (per user)": """
        SELECT Id, ActivityDate, TotalSteps,
               ROUND(AVG(TotalSteps) OVER (
                   PARTITION BY Id ORDER BY ActivityDate
                   ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
               ), 0) AS rolling_7day_avg
        FROM daily_activity
        ORDER BY Id, ActivityDate;
    """,
}


def build_leaderboard_query(metric: str, order: str = "DESC", limit: int = 10) -> str:
    """
    Builds Query 28 dynamically based on the metric picked in the dropdown.
    metric must be one of: TotalSteps, Calories, TotalDistance,
    VeryActiveMinutes, SedentaryMinutes
    order: "DESC" for Top N, "ASC" for Bottom N
    """
    allowed_metrics = {
        "TotalSteps", "Calories", "TotalDistance",
        "VeryActiveMinutes", "SedentaryMinutes",
    }
    if metric not in allowed_metrics:
        raise ValueError(f"metric must be one of {allowed_metrics}")
    if order not in {"ASC", "DESC"}:
        raise ValueError("order must be ASC or DESC")

    return f"""
        SELECT Id, ROUND(AVG({metric}), 1) AS avg_{metric}
        FROM daily_activity
        GROUP BY Id
        ORDER BY avg_{metric} {order}
        LIMIT {limit};
    """