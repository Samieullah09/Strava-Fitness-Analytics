import sqlite3
import pandas as pd

DATA_DIR = "data"
DB_PATH = "fitbit.db"


def load_daily_activity(conn):
    # Read the main daily activity file
    df = pd.read_csv(f"{DATA_DIR}/dailyActivity_merged.csv")
    # Convert text date to real date type
    df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], format="%m/%d/%Y")
    # Remove exact duplicate rows if any
    df = df.drop_duplicates()
    # Save as a table named "daily_activity" inside the database
    df.to_sql("daily_activity", conn, if_exists="replace", index=False)
    print(f"daily_activity: {len(df)} rows loaded")


def load_sleep(conn):
    df = pd.read_csv(f"{DATA_DIR}/sleepDay_merged.csv")
    df["SleepDay"] = pd.to_datetime(df["SleepDay"], format="%m/%d/%Y %I:%M:%S %p").dt.date
    df = df.drop_duplicates()
    df.to_sql("sleep_day", conn, if_exists="replace", index=False)
    print(f"sleep_day: {len(df)} rows loaded")


def load_weight(conn):
    df = pd.read_csv(f"{DATA_DIR}/weightLogInfo_merged.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")
    df = df.drop_duplicates()
    df.to_sql("weight_log", conn, if_exists="replace", index=False)
    print(f"weight_log: {len(df)} rows loaded")


def load_hourly(conn, filename, table_name):
    # Reused for all 3 hourly files: steps, calories, intensities
    df = pd.read_csv(f"{DATA_DIR}/{filename}")
    df["ActivityHour"] = pd.to_datetime(df["ActivityHour"], format="%m/%d/%Y %I:%M:%S %p")
    df = df.drop_duplicates()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"{table_name}: {len(df)} rows loaded")


def load_heartrate_aggregated(conn):
    # Raw file has ~2.48M second-level rows -> too heavy for dashboard queries.
    # So we average it to one value per user per hour before saving.
    df = pd.read_csv(f"{DATA_DIR}/heartrate_seconds_merged.csv")
    df["Time"] = pd.to_datetime(df["Time"], format="%m/%d/%Y %I:%M:%S %p")
    df["ActivityHour"] = df["Time"].dt.floor("h")
    hourly = (
        df.groupby(["Id", "ActivityHour"])["Value"]
        .mean()
        .reset_index()
        .rename(columns={"Value": "AvgHeartRate"})
    )
    hourly.to_sql("heart_rate_hourly", conn, if_exists="replace", index=False)
    print(f"heart_rate_hourly: {len(hourly)} rows loaded (from {len(df)} raw rows)")


def load_mets_aggregated(conn):
    # METs (Metabolic Equivalent of Task) tells exercise intensity.
    # This file is minute-level, so we aggregate it to one value per user per day.
    df = pd.read_csv(f"{DATA_DIR}/minuteMETsNarrow_merged.csv")
    df["ActivityMinute"] = pd.to_datetime(df["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
    df["ActivityDate"] = df["ActivityMinute"].dt.date
    daily = (
        df.groupby(["Id", "ActivityDate"])["METs"]
        .mean()
        .reset_index()
        .rename(columns={"METs": "AvgMETs"})
    )
    daily.to_sql("mets_daily", conn, if_exists="replace", index=False)
    print(f"mets_daily: {len(daily)} rows loaded (from {len(df)} raw rows)")

def data_quality_report(conn):
    # Quick sanity checks -> useful for the "Data Quality" section of the report
    print("\n--- Data Quality Report ---")

    total_users = pd.read_sql("SELECT COUNT(DISTINCT Id) AS n FROM daily_activity", conn)
    print("Unique users:", total_users["n"][0])

    date_range = pd.read_sql(
        "SELECT MIN(ActivityDate) AS start, MAX(ActivityDate) AS end FROM daily_activity", conn
    )
    print("Date range:", date_range["start"][0], "to", date_range["end"][0])

    full_day = pd.read_sql(
        "SELECT COUNT(*) AS n FROM daily_activity WHERE SedentaryMinutes = 1440", conn
    )
    print("Rows where tracker was not worn (SedentaryMinutes = 1440):", full_day["n"][0])

    per_user = pd.read_sql(
        "SELECT Id, COUNT(*) AS days_tracked FROM daily_activity GROUP BY Id", conn
    )
    print("Users with fewer than 20 tracked days:", (per_user["days_tracked"] < 20).sum())


def main():
    conn = sqlite3.connect(DB_PATH)
    load_daily_activity(conn)
    load_sleep(conn)
    load_weight(conn)
    load_hourly(conn, "hourlySteps_merged.csv", "hourly_steps")
    load_hourly(conn, "hourlyCalories_merged.csv", "hourly_calories")
    load_hourly(conn, "hourlyIntensities_merged.csv", "hourly_intensities")
    load_heartrate_aggregated(conn)
    load_mets_aggregated(conn)
    data_quality_report(conn)
    conn.close()
    print(f"\nDone. Database saved at: {DB_PATH}")


if __name__ == "__main__":
    main()