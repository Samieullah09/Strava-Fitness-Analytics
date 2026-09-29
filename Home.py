import streamlit as st
from theme import apply_theme
import streamlit as st
from theme import apply_theme, render_sidebar, render_logo


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Strava Fitness Analytics",
    page_icon="📊",
    layout="wide"
)

apply_theme()
render_sidebar()
render_logo()

# =========================================================
# HOME PAGE FORMATTING
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN CONTENT WIDTH
    ===================================================== */

    .main .block-container {
        max-width: 1200px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       MAIN TITLE
    ===================================================== */

  h1 {
    font-size: 48px !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    letter-spacing: 1px;
    text-align: center !important;
    margin-top: 10px !important;
    margin-bottom: 8px !important;
    text-shadow: 0 0 20px rgba(255,255,255,0.08);
}

h1::after {
    content: "";
    display: block;
    width: 85px;
    height: 3px;
    background: #FC4C02;
    margin: 14px auto 0 auto;
    border-radius: 5px;
    box-shadow: 0 0 12px rgba(252,76,2,0.35);
}


    /* =====================================================
       CAPTION
    ===================================================== */

    [data-testid="stCaptionContainer"] {
    color: #858585 !important;
    font-size: 14px !important;
    text-align: center !important;
    letter-spacing: 0.3px;
    margin-top: 8px !important;
    margin-bottom: 55px !important;
}


    /* =====================================================
       SECTION HEADINGS
    ===================================================== */

    h2 {
    font-size: 28px !important;
    color: #F1F1F1 !important;
    font-weight: 700 !important;

    margin-top: 34px !important;
    margin-bottom: 16px !important;

    padding-left: 16px !important;

    border-left: 3px solid #FC4C02;
    box-shadow: 0 0 8px rgba(252, 76, 2, 0.18);

    line-height: 1.25 !important;
}


    h3 {
    font-size: 22px !important;

    color: #FFFFFF !important;

    font-weight: 700 !important;

    letter-spacing: 0.3px;

    margin-top: 0 !important;

    margin-bottom: 10px !important;

    padding-bottom: 10px !important;

    border-bottom: 1px solid rgba(252, 76, 2, 0.35);

    /* White glow */
    text-shadow:
        0 0 4px rgba(255,255,255,0.35),
        0 0 9px rgba(255,255,255,0.18),
        0 0 16px rgba(255,255,255,0.08);

    transition: all 0.25s ease;
}


    /* =====================================================
       NORMAL TEXT
    ===================================================== */

    .stMarkdown p {
        color: #B3B3B3;

        font-size: 15px;

        line-height: 1.7;
    }


    /* =====================================================
       BUSINESS TASK AREA
    ===================================================== */

    /* Give normal content some spacing */

    [data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }


    /* =====================================================
       NAVIGATION COLUMNS
    ===================================================== */

    /* Column backgrounds */

    [data-testid="column"] {
        background:
            linear-gradient(
                145deg,
                rgba(24,24,24,0.72),
                rgba(7,7,7,0.72)
            );

        border: 1px solid rgba(252,76,2,0.20);

        border-radius: 10px;

        padding: 18px 20px;

        min-height: 145px;

        box-shadow:
            0 8px 24px rgba(0,0,0,0.25);

        margin-bottom: 10px;
    }


    /* =====================================================
       SUBHEADINGS INSIDE CARDS
    ===================================================== */

    [data-testid="column"] h3 {
    margin-top: 0 !important;

    color: #FFFFFF !important;

    padding-left: 2px !important;
}


    /* =====================================================
       LISTS
    ===================================================== */

    ul {
        color: #B7B7B7 !important;

        line-height: 1.8;
    }

    li {
        color: #B7B7B7 !important;
    }


    /* Orange table names */

    li strong {
        color: #FC4C02 !important;
    }


    /* =====================================================
       DIVIDER
    ===================================================== */

    hr {
        border: none !important;

        border-top:
            1px solid rgba(255,255,255,0.10) !important;

        margin:
            25px 0 !important;
    }


    /* =====================================================
       FUTURE WORK / LIMITATIONS LIST
    ===================================================== */

    [data-testid="stMarkdownContainer"] ul {
        padding-left: 22px;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {
        background:
            rgba(3,3,3,0.97) !important;

        border-right:
            1px solid rgba(255,255,255,0.08);
    }


    /* Sidebar navigation */

    section[data-testid="stSidebar"] a {
        color: #D0D0D0 !important;
    }


    /* =====================================================
       SMALL ORANGE ACCENT
    ===================================================== */

    .stMarkdown strong {
        color: #FC4C02;
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 768px) {

        h1 {
            font-size: 32px !important;
        }

        h2 {
            font-size: 24px !important;
        }

        [data-testid="column"] {
            margin-bottom: 15px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.title("Strava Fitness Analytics")

st.caption(
    "Fitbit fitness tracker data  •  33 users  •  12 Apr — 12 May 2016"

)

# =========================================================
# DATABASE OVERVIEW
# =========================================================

st.header("Database Overview")

db1, db2, db3, db4 = st.columns(4)

with db1:
    st.metric(
        "Users",
        "33"
    )

with db2:
    st.metric(
        "Analytical Tables",
        "8"
    )

with db3:
    st.metric(
        "SQL Questions",
        "30"
    )

with db4:
    st.metric(
        "Data Period",
        "1 Month"
    )


# =========================================================
# BUSINESS TASK
# =========================================================

st.header("Business Task")

st.write(
    "Analyze how users engage with their fitness tracker "
    "(steps, calories, sleep, heart rate, and weight) to "
    "uncover activity patterns and provide recommendations "
    "for improving user engagement."
)


# =========================================================
# WHAT'S IN THIS APP
# =========================================================

st.header("What's in this app")

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Dashboard")

    st.write(
        "Visual charts covering activity, calories, "
        "sleep, intensity, and hourly patterns."
    )


with col2:

    st.subheader("🛢️ SQL Playground")

    st.write(
        "30 predefined SQL questions covering activity, "
        "calories, intensity, sleep, heart rate, "
        "weight and advanced SQL."
    )


# =========================================================
# DATA DESCRIPTION
# =========================================================

with st.expander("📄 Data Description"):
    st.write(
        "The raw dataset has 18 CSV files. Several are duplicates or subsets of each "
        "other (e.g. dailyCalories, dailyIntensities and dailySteps are already included "
        "in dailyActivity). After removing duplicates, 8 analytical tables were built:"
    )
    st.markdown(
        """
- **daily_activity** — steps, distance, intensity minutes, calories (per user/day)
- **sleep_day** — sleep records (per user/day)
- **weight_log** — weight and BMI (only ~8 users logged this)
- **hourly_steps / hourly_calories / hourly_intensities** — per user/hour
- **heart_rate_hourly** — aggregated from 2.48M raw second-level readings
- **mets_daily** — aggregated from 1.3M raw minute-level METs readings
"""
    )



# =========================================================
# LIMITATIONS
# =========================================================

with st.expander("⚠️ Limitations"):
    st.markdown(
        """
- Only **33 users** and **1 month** of data — results may not generalize to a wider population.
- No demographic information such as age, sex, or profession — users cannot be segmented by these factors.
- **Weight data** covers very few users — BMI insights are not statistically strong.
- Not every user has a full 31 days tracked; some rows indicate the tracker was not worn.
"""
    )


# =========================================================
# FUTURE WORK
# =========================================================

with st.expander("🚀 Future Work"):
    st.markdown(
        """
- Connect to a live fitness-tracker API instead of a static CSV export.
- Schedule a daily job to refresh the database automatically.
- Monitor for data drift, such as sudden changes in active users.
- Expand the dataset to a larger and more demographically diverse user base.
"""
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "STRAVA FITNESS ANALYTICS  •  SQL + STREAMLIT  •  FITNESS DATA PROJECT"
)