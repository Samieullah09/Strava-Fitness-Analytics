import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

from theme import apply_theme, render_sidebar, render_logo



# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout="wide"
)

apply_theme()
render_sidebar()
render_logo()
from user_labels import get_label_map
from queries import build_leaderboard_query

# =========================================================
# DASHBOARD-SPECIFIC STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN CONTENT
    ===================================================== */

    .main .block-container {
        max-width: 1200px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       DASHBOARD HERO
    ===================================================== */

    h1 {
        text-align: center !important;

        font-size: 48px !important;

        font-weight: 800 !important;

        color: #FFFFFF !important;

        letter-spacing: 1px;

        margin-top: 8px !important;

        margin-bottom: 8px !important;

        text-shadow:
            0 0 5px rgba(255,255,255,0.25),
            0 0 12px rgba(255,255,255,0.10);
    }


    h1::after {
        content: "";

        display: block;

        width: 75px;

        height: 3px;

        background: #FC4C02;

        margin: 14px auto 0 auto;

        border-radius: 5px;

        box-shadow:
            0 0 10px rgba(252,76,2,0.35);
    }


    /* Small subtitle under Dashboard */

    .dashboard-subtitle {
        text-align: center;

        color: #858585;

        font-size: 13px;

        letter-spacing: 1.2px;

        margin-top: 12px;

        margin-bottom: 30px;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {
        background: rgba(3,3,3,0.97) !important;

        border-right:
            1px solid rgba(252,76,2,0.18);
    }


    section[data-testid="stSidebar"] label {
        color: #BDBDBD !important;

        font-size: 13px !important;
    }


    /* =====================================================
       TABS
    ===================================================== */

    button[data-baseweb="tab"] {
        color: #A5A5A5 !important;

        font-size: 13px !important;

        font-weight: 600 !important;

        padding-left: 8px !important;

        padding-right: 8px !important;

        transition: all 0.2s ease;
    }


    button[data-baseweb="tab"]:hover {
        color: #FFFFFF !important;
    }


    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;

        text-shadow:
            0 0 7px rgba(255,255,255,0.25);
    }


    div[data-baseweb="tab-highlight"] {
        background-color: #FC4C02 !important;

        height: 3px !important;

        box-shadow:
            0 0 8px rgba(252,76,2,0.45);
    }


    /* =====================================================
       KPI CARDS
    ===================================================== */

    /* Dashboard KPI cards */
div[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        rgba(20, 21, 25, 0.96),
        rgba(8, 9, 12, 0.96)
    );

    border: 1px solid rgba(255, 255, 255, 0.08);
    border-left: 3px solid #FC4C02;

    border-radius: 10px;

    padding: 16px 18px;

    min-height: 92px;

    box-shadow:
        0 0 18px rgba(252, 76, 2, 0.08),
        inset 0 0 20px rgba(255, 255, 255, 0.015);

    transition: all 0.2s ease;
}

/* KPI label */
div[data-testid="stMetricLabel"] {
    color: #9da3ad !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1.3px !important;
}

/* KPI value */
div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 27px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px;
}


    /* =====================================================
       CHART AREA
    ===================================================== */

    div[data-testid="stPlotlyChart"] {
        background:
            linear-gradient(
                145deg,
                rgba(17,17,17,0.65),
                rgba(5,5,5,0.65)
            );

        border:
            1px solid rgba(255,255,255,0.07);

        border-radius: 10px;

        padding: 5px;

        margin-top: 8px;

        margin-bottom: 12px;
    }


    /* =====================================================
       TAB CONTENT HEADINGS
    ===================================================== */

    h2 {
        color: #F1F1F1 !important;

        border-left:
            3px solid #FC4C02;

        padding-left: 15px !important;

        margin-top: 25px !important;

        margin-bottom: 18px !important;
    }


    h3 {
        color: #FFFFFF !important;
    }


    /* =====================================================
       SELECTBOX / RADIO
    ===================================================== */

    div[data-baseweb="select"] > div {
        background-color:
            rgba(18,18,18,0.90) !important;

        border-color:
            rgba(255,255,255,0.10) !important;
    }


    div[data-baseweb="select"] span {
        color: #D0D0D0 !important;
    }


    /* =====================================================
       RECOMMENDATION BOX
    ===================================================== */

    div[data-testid="stAlert"] {
        background:
            rgba(252,76,2,0.07) !important;

        border-left:
            4px solid #FC4C02 !important;

        border-top:
            1px solid rgba(252,76,2,0.12);

        border-right:
            1px solid rgba(252,76,2,0.08);

        border-bottom:
            1px solid rgba(252,76,2,0.08);

        border-radius: 8px;

        box-shadow:
            0 0 16px rgba(252,76,2,0.08);
    }


    /* =====================================================
       DIVIDERS
    ===================================================== */

    hr {
        border:
            none !important;

        border-top:
            1px solid rgba(255,255,255,0.09) !important;

        margin:
            24px 0 !important;
    }


    /* =====================================================
       CAPTION
    ===================================================== */

    .stCaption {
        color: #858585 !important;
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 900px) {

        h1 {
            font-size: 38px !important;
        }

        button[data-baseweb="tab"] {
            font-size: 11px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DASHBOARD TITLE
# =========================================================

st.title("Dashboard")

st.markdown(
    """
    <div class="dashboard-subtitle">
        FITNESS DATA ANALYTICS&nbsp;&nbsp;•&nbsp;&nbsp;
        ACTIVITY&nbsp;&nbsp;•&nbsp;&nbsp;
        CALORIES&nbsp;&nbsp;•&nbsp;&nbsp;
        SLEEP&nbsp;&nbsp;•&nbsp;&nbsp;
        HEART RATE
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATABASE CONNECTION
# =========================================================

conn = sqlite3.connect("fitbit.db")

WEEKDAY_ORDER = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


# =========================================================
# SIDEBAR FILTER
# =========================================================

st.sidebar.markdown("### Dashboard Filter")

label_map = get_label_map(conn)

user_ids = list(label_map.keys())

selected_user = st.sidebar.selectbox(
    "View data for:",
    ["All Users"] + user_ids,
    format_func=lambda x: label_map.get(x, x)
)

user_filter = (
    ""
    if selected_user == "All Users"
    else f"WHERE Id = {selected_user}"
)


# =========================================================
# DATA LOADER
# =========================================================

def load(table):
    return pd.read_sql(
        f"SELECT * FROM {table} {user_filter}",
        conn
    )


# =========================================================
# LOAD DATA
# =========================================================

activity = load("daily_activity")
sleep = load("sleep_day")
hourly_steps = load("hourly_steps")
hourly_calories = load("hourly_calories")
heart_rate = load("heart_rate_hourly")
weight = load("weight_log")


# =========================================================
# DATA PREPARATION
# =========================================================

activity["Weekday"] = pd.to_datetime(
    activity["ActivityDate"]
).dt.day_name()


# =========================================================
# PLOTLY THEME HELPER
# =========================================================

def style_chart(fig):

    fig.update_layout(
        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="#BDBDBD",
            family="Arial"
        ),

        title=dict(
            font=dict(
                color="#FFFFFF",
                size=17
            ),
            x=0.02
        ),

        margin=dict(
            l=45,
            r=25,
            t=55,
            b=45
        ),

        hoverlabel=dict(
            bgcolor="#171717",
            font_color="#FFFFFF"
        ),

        legend=dict(
            font=dict(
                color="#BDBDBD"
            )
        )
    )

    fig.update_xaxes(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.08)"
    )

    fig.update_yaxes(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.08)"
    )

    return fig


def show_chart(fig):
    st.plotly_chart(
        style_chart(fig),
        use_container_width=True
    )


# =========================================================
# TABS
# =========================================================

tabs = st.tabs(
    [
        "Overview",
        "Daily Activity",
        "Calories",
        "Intensity",
        "Distance",
        "Hourly",
        "Sleep",
        "Heart Rate",
        "Weight/BMI",
        "Leaderboard"
    ]
)


# =========================================================
# OVERVIEW
# =========================================================


with tabs[0]:

    st.markdown("### Dashboard Summary")

    total_users = pd.read_sql(
        "SELECT COUNT(DISTINCT Id) AS n FROM daily_activity",
        conn
    )["n"][0]

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "TOTAL USERS",
        f"{total_users:,}"
    )

    c2.metric(
        "AVG STEPS",
        f"{activity['TotalSteps'].mean():,.0f}"
    )

    c3.metric(
        "AVG CALORIES",
        f"{activity['Calories'].mean():,.0f}"
    )

    c4.metric(
        "AVG DISTANCE",
        f"{activity['TotalDistance'].mean():.2f} km"
    )

    c5.metric(
        "AVG SLEEP",
        f"{sleep['TotalMinutesAsleep'].mean():,.0f} min"
        if len(sleep)
        else "No data"
    )

    st.caption(
        "A quick summary of overall fitness activity across the selected users."
    )
# =========================================================
# DAILY ACTIVITY
# =========================================================

with tabs[1]:

    c1, c2 = st.columns(2)

    with c1:

        daily_steps = activity.groupby(
            "ActivityDate"
        )["TotalSteps"].mean()

        show_chart(
            px.line(
                daily_steps,
                title="Daily Steps Trend",
		labels={"value": "Steps", "index": "Date"}
            )
        )

    with c2:

        weekday_steps = (
            activity.groupby("Weekday")["TotalSteps"]
            .mean()
            .reindex(WEEKDAY_ORDER)
        )

        show_chart(
            px.bar(
                weekday_steps,
                title="Average Steps by Weekday",
		labels={"value": "Avg Steps", "index": "Weekday"}
            )
        )


# =========================================================
# CALORIES
# =========================================================

with tabs[2]:

    c1, c2 = st.columns(2)

    with c1:

        daily_cal = activity.groupby(
            "ActivityDate"
        )["Calories"].mean()

        show_chart(
            px.line(
                daily_cal,
                title="Calories Trend",
		labels={"value": "Calories (kcal)", "index": "Date"}
            )
        )

    with c2:

        show_chart(
            px.scatter(
                activity,
                x="TotalSteps",
                y="Calories",
                title="Steps vs Calories Burned",
		labels={"TotalSteps": "Steps", "Calories": "Calories (kcal)"}
            )
        )


# =========================================================
# INTENSITY
# =========================================================

with tabs[3]:

    c1, c2 = st.columns(2)

    with c1:

        intensity = pd.DataFrame(
            {
                "Type": [
                    "Sedentary",
                    "Lightly Active",
                    "Fairly Active",
                    "Very Active"
                ],

                "Minutes": [
                    activity["SedentaryMinutes"].mean(),
                    activity["LightlyActiveMinutes"].mean(),
                    activity["FairlyActiveMinutes"].mean(),
                    activity["VeryActiveMinutes"].mean()
                ]
            }
        )

        show_chart(
            px.pie(
                intensity,
                names="Type",
                values="Minutes",
                title="Time Spent by Intensity Level",
                hole=0.4
            )
        )

    with c2:

        active_vs_sedentary = pd.DataFrame(
            {
                "Type": [
                    "Sedentary",
                    "Active"
                ],

                "Minutes": [
                    activity["SedentaryMinutes"].mean(),

                    (
                        activity["LightlyActiveMinutes"]
                        + activity["FairlyActiveMinutes"]
                        + activity["VeryActiveMinutes"]
                    ).mean()
                ]
            }
        )

        show_chart(
            px.bar(
                active_vs_sedentary,
                x="Type",
                y="Minutes",
                title="Sedentary vs Active Time",
		labels={"Minutes": "Avg Minutes/Day"}
            )
        )


# =========================================================
# DISTANCE
# =========================================================

with tabs[4]:

    c1, c2 = st.columns(2)

    with c1:

        daily_distance = activity.groupby(
            "ActivityDate"
        )["TotalDistance"].mean()

        show_chart(
            px.line(
                daily_distance,
                title="Distance Trend",
		labels={"value": "Distance (km)", "index": "Date"}
            )
        )

    with c2:

        show_chart(
            px.scatter(
                activity,
                x="TotalSteps",
                y="TotalDistance",
                title="Steps vs Distance",
		labels={"TotalSteps": "Steps", "TotalDistance": "Distance (km)"}
            )
        )


# =========================================================
# HOURLY
# =========================================================

with tabs[5]:

    c1, c2, c3 = st.columns(3)

    with c1:

        if len(hourly_steps):

            hourly_steps["Hour"] = pd.to_datetime(
                hourly_steps["ActivityHour"]
            ).dt.hour

            avg = (
                hourly_steps
                .groupby("Hour")["StepTotal"]
                .mean()
            )

            show_chart(
                px.bar(
                    avg,
                    title="Average Steps by Hour",
		    labels={"value": "Avg Steps", "Hour": "Hour of Day (24h)"}
                )
            )

    with c2:

        if len(hourly_calories):

            hourly_calories["Hour"] = pd.to_datetime(
                hourly_calories["ActivityHour"]
            ).dt.hour

            avg = (
                hourly_calories
                .groupby("Hour")["Calories"]
                .mean()
            )

            show_chart(
                px.bar(
                    avg,
                    title="Average Calories by Hour",
		    labels={"value": "Avg Calories (kcal)", "Hour": "Hour of Day (24h)"}
                )
            )

    with c3:

        if len(hourly_steps):

            def part_of_day(h):

                if 5 <= h <= 11:
                    return "Morning"

                if 12 <= h <= 16:
                    return "Afternoon"

                if 17 <= h <= 20:
                    return "Evening"

                return "Night"

            hourly_steps["Part"] = (
                hourly_steps["Hour"]
                .apply(part_of_day)
            )

            part_avg = (
                hourly_steps
                .groupby("Part")["StepTotal"]
                .mean()
            )

            show_chart(
                px.bar(
                    part_avg,
                    title="Activity by Part of Day",
		    labels={"value": "Avg Steps", "Part": "Time of Day"}
                )
            )


# =========================================================
# SLEEP
# =========================================================

with tabs[6]:

    if len(sleep):

        sleep["Weekday"] = pd.to_datetime(
            sleep["SleepDay"]
        ).dt.day_name()

        c1, c2 = st.columns(2)

        with c1:

            sleep_by_weekday = (
                sleep
                .groupby("Weekday")["TotalMinutesAsleep"]
                .mean()
                .reindex(WEEKDAY_ORDER)
            )

            show_chart(
                px.bar(
                    sleep_by_weekday,
                    title="Sleep Duration by Weekday",
		    labels={"value": "Minutes Asleep", "Weekday": "Day"}
                )
            )

        with c2:

            sleep["SleepDay_str"] = (
                pd.to_datetime(sleep["SleepDay"])
                .dt.date
                .astype(str)
            )

            activity["ActivityDate_str"] = (
                pd.to_datetime(activity["ActivityDate"])
                .dt.date
                .astype(str)
            )

            merged = pd.merge(
                sleep,
                activity,
                left_on=["Id", "SleepDay_str"],
                right_on=["Id", "ActivityDate_str"]
            )

            show_chart(
                px.scatter(
                    merged,
                    x="TotalMinutesAsleep",
                    y="TotalSteps",
                    title="Sleep vs Steps",
		    labels={"TotalMinutesAsleep": "Minutes Asleep", "TotalSteps": "Steps"}
                )
            )

        gap = (
            sleep["TotalTimeInBed"]
            - sleep["TotalMinutesAsleep"]
        ).mean()

        st.metric(
            "Avg Time Awake in Bed",
            f"{gap:.0f} min"
        )

    else:

        st.caption(
            "No sleep data for this user."
        )


# =========================================================
# HEART RATE
# =========================================================

with tabs[7]:

    if len(heart_rate):

        heart_rate["Hour"] = pd.to_datetime(
            heart_rate["ActivityHour"]
        ).dt.hour

        avg_hr = (
            heart_rate
            .groupby("Hour")["AvgHeartRate"]
            .mean()
        )

        show_chart(
            px.line(
                avg_hr,
                title="Average Heart Rate by Hour",
		labels={"value": "Heart Rate (bpm)", "Hour": "Hour of Day (24h)"}
            )
        )

    else:

        st.caption(
            "No heart rate data for this user."
        )


# =========================================================
# WEIGHT / BMI
# =========================================================

with tabs[8]:

    if len(weight):

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Average BMI",
                f"{weight['BMI'].mean():.1f}"
            )

        with c2:

            show_chart(
                px.line(
                    weight,
                    x="Date",
                    y="WeightKg",
                    title="Weight Trend (kg)",
		    labels={"WeightKg": "Weight (kg)"}
                )
            )

    else:

        st.caption(
            "No weight data for this user "
            "(only ~8 of 33 users logged weight)."
        )


# =========================================================
# LEADERBOARD
# =========================================================

with tabs[9]:

    st.caption(
        "Leaderboard always shows all users, "
        "regardless of the sidebar filter."
    )

    lc1, lc2 = st.columns(2)

    with lc1:

        metric = st.selectbox(
            "Metric:",
            [
                "TotalSteps",
                "Calories",
                "TotalDistance",
                "VeryActiveMinutes",
                "SedentaryMinutes"
            ]
        )

    with lc2:

        order_label = st.radio(
            "Show:",
            ["Top 10", "Bottom 10"],
            horizontal=True
        )

    order = (
        "DESC"
        if order_label == "Top 10"
        else "ASC"
    )

    sql = build_leaderboard_query(
        metric,
        order,
        10
    )

    board = pd.read_sql(
        sql,
        conn
    )

    board.insert(
        0,
        "User",
        board["Id"].map(label_map)
    )

    show_chart(
        px.bar(
            board,
            x="User",
            y=board.columns[-1],
            title=f"{order_label} by {metric}",
	    labels={board.columns[-1]: f"Avg {metric}"}    
        )
    )


# =========================================================
# RECOMMENDATION
# =========================================================

st.divider()

if len(hourly_steps):

    if "Hour" not in hourly_steps.columns:

        hourly_steps["Hour"] = pd.to_datetime(
            hourly_steps["ActivityHour"]
        ).dt.hour

    peak_hour = (
        hourly_steps
        .groupby("Hour")["StepTotal"]
        .mean()
        .idxmax()
    )

else:

    peak_hour = None


low_day = (
    activity
    .groupby("Weekday")["TotalSteps"]
    .mean()
    .reindex(WEEKDAY_ORDER)
    .idxmin()
)


st.info(
    f"💡 **Recommendation:** Activity is lowest on **{low_day}**"
    + (
        f" and peaks around **{peak_hour}:00**."
        if peak_hour is not None
        else "."
    )
    + " Consider scheduling reminders or challenges around "
      "these times to boost engagement."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "FITNESS DATA ANALYTICS  •  STREAMLIT DASHBOARD  •  SQL + VISUAL ANALYTICS"
)


# =========================================================
# CLOSE DATABASE
# =========================================================

conn.close()