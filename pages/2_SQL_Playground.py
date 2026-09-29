import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

from user_labels import get_label_map
from theme import apply_theme, render_sidebar, render_logo


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SQL Playground",
    page_icon="🛢️",
    layout="wide"
)

apply_theme()
render_sidebar()
render_logo()

from queries import QUERIES, build_leaderboard_query
# =========================================================
# PAGE-SPECIFIC STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- SQL PAGE TITLE ---------- */

    h1 {
        font-size: 46px !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        text-align: center !important;

        margin-top: 18px !important;
        margin-bottom: 8px !important;

        letter-spacing: 1px;

        text-shadow:
            0 0 4px rgba(255,255,255,0.35),
            0 0 9px rgba(255,255,255,0.18),
            0 0 16px rgba(255,255,255,0.08);
    }

    h1::after {
        content: "";
        display: block;

        width: 70px;
        height: 3px;

        background: #FC4C02;

        margin: 14px auto 0 auto;

        border-radius: 5px;

        box-shadow:
            0 0 12px rgba(252,76,2,0.35);
    }


    /* ---------- PAGE CAPTION ---------- */

    [data-testid="stCaptionContainer"] {
        color: #858585 !important;

        font-size: 14px !important;

        text-align: center !important;

        letter-spacing: 0.3px;

        margin-top: 8px !important;
        margin-bottom: 34px !important;
    }


    /* ---------- QUESTION LABEL ---------- */

    label {
        color: #BFC3CA !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }


    /* ---------- SELECT BOX ---------- */

    div[data-baseweb="select"] > div {
        background: rgba(18, 19, 23, 0.96) !important;

        border: 1px solid rgba(255,255,255,0.08) !important;

        border-radius: 7px !important;
    }


    /* ---------- SQL CODE BLOCK ---------- */

    div[data-testid="stCodeBlock"] {
        border: 1px solid rgba(252,76,2,0.16);

        border-left: 3px solid #FC4C02;

        border-radius: 8px;

        box-shadow:
            0 0 16px rgba(252,76,2,0.06);
    }


    /* ---------- RUN QUERY BUTTON ---------- */

    div.stButton > button {
        background: #FC4C02 !important;

        color: #FFFFFF !important;

        border: none !important;

        border-radius: 7px !important;

        font-weight: 700 !important;

        padding: 9px 20px !important;

        box-shadow:
            0 0 12px rgba(252,76,2,0.18);

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: #FF5A16 !important;

        box-shadow:
            0 0 18px rgba(252,76,2,0.30);
    }


    /* ---------- RESULT SECTION HEADINGS ---------- */

    h2 {
        font-size: 25px !important;

        color: #F1F1F1 !important;

        font-weight: 700 !important;

        margin-top: 32px !important;
        margin-bottom: 15px !important;

        padding-left: 14px !important;

        border-left: 3px solid #FC4C02;

        line-height: 1.25 !important;
    }


    /* ---------- DATAFRAME ---------- */

    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(255,255,255,0.07);

        border-radius: 8px;

        overflow: hidden;
    }


    /* ---------- METRIC RESULT ---------- */

    div[data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            rgba(20,21,25,0.96),
            rgba(8,9,12,0.96)
        );

        border: 1px solid rgba(255,255,255,0.08);

        border-left: 3px solid #FC4C02;

        border-radius: 9px;

        padding: 15px 18px;

        box-shadow:
            0 0 16px rgba(252,76,2,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #9DA3AD !important;

        font-size: 11px !important;

        font-weight: 700 !important;

        letter-spacing: 1.1px !important;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;

        font-size: 27px !important;

        font-weight: 700 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE HEADER
# =========================================================

st.title("SQL Playground")

st.caption(
    "Explore 30 predefined SQL questions, inspect the query, and run it against the fitness database."
)


# =========================================================
# DATABASE CONNECTION
# =========================================================

conn = sqlite3.connect("fitbit.db")


# =========================================================
# QUESTION SELECTION
# =========================================================

question = st.selectbox(
    "Choose a question:",
    list(QUERIES.keys())
)


# =========================================================
# QUESTION 28 — DYNAMIC LEADERBOARD
# =========================================================

if question.startswith("28."):

    st.markdown("### Leaderboard Controls")

    c1, c2 = st.columns(2)

    with c1:
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

    with c2:
        order_label = st.radio(
            "Show:",
            ["Top 10", "Bottom 10"],
            horizontal=True
        )

    order = "DESC" if order_label == "Top 10" else "ASC"

    sql = build_leaderboard_query(
        metric,
        order,
        10
    )

else:

    sql = QUERIES[question]


# =========================================================
# SQL DISPLAY
# =========================================================

st.markdown("### SQL Query")

st.code(
    sql.strip(),
    language="sql"
)


# =========================================================
# RUN QUERY
# =========================================================

if st.button("▶ Run Query"):

    df = pd.read_sql(
        sql,
        conn
    )


    # -----------------------------------------------------
    # FRIENDLY USER LABEL
    # -----------------------------------------------------

    if "Id" in df.columns:

        label_map = get_label_map(conn)

        df.insert(
            0,
            "User",
            df["Id"].map(label_map)
        )


    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------

    st.markdown("### Query Result")

    st.dataframe(
        df,
        use_container_width=True
    )


    # =====================================================
    # AUTO VISUALIZATION
    # =====================================================

    chart_df = (
        df.drop(columns=["Id"])
        if "Id" in df.columns
        else df.copy()
    )


    # -----------------------------------------------------
    # CASE 1 — SINGLE VALUE
    # -----------------------------------------------------

    if chart_df.shape == (1, 1):

        st.markdown("### Result Summary")

        st.metric(
            chart_df.columns[0],
            chart_df.iloc[0, 0]
        )


    # -----------------------------------------------------
    # CASE 2 — ONE ROW, MULTIPLE COLUMNS
    # -----------------------------------------------------

    elif (
        chart_df.shape[0] == 1
        and chart_df.shape[1] > 1
    ):

        melted = chart_df.melt(
            var_name="Category",
            value_name="Value"
        )

        fig = px.bar(
            melted,
            x="Category",
            y="Value",
            title=question
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # -----------------------------------------------------
    # CASE 3 — TWO COLUMNS
    # -----------------------------------------------------

    elif chart_df.shape[1] == 2:

        col_x, col_y = chart_df.columns


        if len(chart_df) > 100:

            fig = px.scatter(
                chart_df,
                x=col_x,
                y=col_y,
                title=f"{col_x} vs {col_y}"
            )


        elif (
            "date" in col_x.lower()
            or "hour" in col_x.lower()
        ):

            fig = px.line(
                chart_df,
                x=col_x,
                y=col_y,
                title=question
            )


        else:

            fig = px.bar(
                chart_df,
                x=col_x,
                y=col_y,
                title=question
            )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # -----------------------------------------------------
    # CASE 4 — USER BASED RESULT
    # -----------------------------------------------------

    elif (
        "User" in chart_df.columns
        and chart_df.shape[0] <= 50
    ):

        metric_columns = [
            c for c in chart_df.columns
            if c != "User"
        ]

        if metric_columns:

            metric_col = metric_columns[0]

            fig = px.bar(
                chart_df,
                x="User",
                y=metric_col,
                title=question
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # -----------------------------------------------------
    # CASE 5 — TOO COMPLEX FOR AUTO CHART
    # -----------------------------------------------------

    else:

        st.caption(
            "Table above has too many rows or columns for a clean automatic chart."
        )


# =========================================================
# CLOSE DATABASE
# =========================================================

conn.close()