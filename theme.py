import os
import base64 
from pathlib import Path
import streamlit as st


def apply_theme():

 

    # =========================================================
    # LOAD SPORTS BACKGROUND
    # sports_bg.jpg is in project ROOT folder
    # =========================================================

    bg_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sports_bg.jpg"
    )

    if os.path.exists(bg_path):

        with open(bg_path, "rb") as image_file:
            encoded_image = base64.b64encode(
                image_file.read()
            ).decode()

        background_image = (
            f"url('data:image/png;base64,{encoded_image}')"
        )

    else:
        background_image = "none"


    # =========================================================
    # GLOBAL THEME
    # =========================================================

    st.markdown(
        f"""
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&display=swap'
        );


        /* =====================================================
           SPORTS BACKGROUND
           ===================================================== */

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.60),
                    rgba(0, 0, 0, 0.60)
                ),
                {background_image} !important;

            background-position:
                center center !important;

            background-size:
                cover !important;

            background-repeat:
                no-repeat !important;

            background-attachment:
                fixed !important;
        }}


        [data-testid="stAppViewContainer"] {{
            background:
                transparent !important;
        }}


        [data-testid="stAppViewContainer"] > .main {{
            background:
                transparent !important;
        }}


        .main {{
            background:
                transparent !important;
        }}


        [data-testid="stHeader"] {{
            background:
                transparent !important;
        }}


        /* =====================================================
           GLOBAL HEADINGS
           ===================================================== */

        h1,
        h2,
        h3 {{
            font-family:
                'Rajdhani',
                sans-serif !important;
        }}


        /* =====================================================
           HOME TITLE
           ===================================================== */

        h1 {{
            font-size:
                48px !important;

            font-weight:
                800 !important;

            color:
                #FFFFFF !important;

            letter-spacing:
                1px;

            text-align:
                center !important;

            margin-top:
                10px !important;

            margin-bottom:
                8px !important;

            text-shadow:
                0 0 4px rgba(255,255,255,0.35),
                0 0 9px rgba(255,255,255,0.18),
                0 0 16px rgba(255,255,255,0.08);
        }}


        h1::after {{
            content:
                "";

            display:
                block;

            width:
                85px;

            height:
                3px;

            background:
                #FC4C02;

            margin:
                14px auto 0 auto;

            border-radius:
                5px;

            box-shadow:
                0 0 12px rgba(252,76,2,0.35);
        }}


        /* =====================================================
           CAPTION
           ===================================================== */

        [data-testid="stCaptionContainer"] {{
            color:
                #858585 !important;

            font-size:
                14px !important;

            text-align:
                center !important;

            letter-spacing:
                0.3px;

            margin-top:
                8px !important;

            margin-bottom:
                55px !important;
        }}


        /* =====================================================
           SECTION HEADINGS
           ===================================================== */

        h2 {{
            font-size:
                28px !important;

            color:
                #F1F1F1 !important;

            font-weight:
                700 !important;

            margin-top:
                34px !important;

            margin-bottom:
                16px !important;

            padding-left:
                16px !important;

            border-left:
                3px solid #FC4C02;

            box-shadow:
                0 0 8px rgba(252,76,2,0.18);

            line-height:
                1.25 !important;
        }}


        /* =====================================================
           FEATURE HEADINGS
           ===================================================== */

        h3 {{
            font-size:
                22px !important;

            color:
                #FFFFFF !important;

            font-weight:
                700 !important;

            letter-spacing:
                0.3px;

            margin-top:
                0 !important;

            margin-bottom:
                10px !important;

            padding-bottom:
                10px !important;

            border-bottom:
                1px solid rgba(252,76,2,0.35);

            text-shadow:
                0 0 4px rgba(255,255,255,0.35),
                0 0 9px rgba(255,255,255,0.18),
                0 0 16px rgba(255,255,255,0.08);
        }}


        /* =====================================================
           HOME FEATURE CARDS
           ===================================================== */

        [data-testid="column"] {{
            background:
                linear-gradient(
                    145deg,
                    rgba(24,24,24,0.72),
                    rgba(7,7,7,0.72)
                );

            border:
                1px solid rgba(252,76,2,0.20);

            border-radius:
                10px;

            padding:
                18px 20px;

            min-height:
                145px;

            box-shadow:
                0 8px 24px rgba(0,0,0,0.25);

            margin-bottom:
                10px;
        }}


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {{
            background:
                linear-gradient(
                    180deg,
                    rgba(7,8,10,0.99),
                    rgba(10,10,12,0.99),
                    rgba(5,6,8,0.99)
                ) !important;

            border-right:
                1px solid rgba(252,76,2,0.22);

            box-shadow:
                8px 0 30px rgba(0,0,0,0.28);
        }}


        section[data-testid="stSidebar"] > div {{
            padding-top:
                1rem !important;

            padding-left:
                0.65rem !important;

            padding-right:
                0.65rem !important;
        }}


        /* =====================================================
           SIDEBAR NAVIGATION
           ===================================================== */

        section[data-testid="stSidebar"] ul {{
            padding-top:
                4px;
        }}


        section[data-testid="stSidebar"] li {{
            margin-bottom:
                3px;
        }}


        section[data-testid="stSidebar"] a {{
            border-radius:
                7px !important;

            transition:
                all 0.2s ease !important;
        }}


        section[data-testid="stSidebar"] a:hover {{
            background:
                rgba(252,76,2,0.10) !important;
        }}


        section[data-testid="stSidebar"] a[aria-current="page"] {{
            background:
                linear-gradient(
                    90deg,
                    rgba(252,76,2,0.18),
                    rgba(252,76,2,0.04)
                ) !important;

            border-left:
                3px solid #FC4C02 !important;

            box-shadow:
                0 0 12px rgba(252,76,2,0.08);
        }}


        /* =====================================================
           SIDEBAR BRAND
           ===================================================== */

        .sidebar-brand {{
            margin-top:
                18px;

            margin-bottom:
                18px;

            padding:
                14px 12px 15px 12px;

            background:
                linear-gradient(
                    145deg,
                    rgba(20,21,25,0.95),
                    rgba(8,9,11,0.95)
                );

            border:
                1px solid rgba(255,255,255,0.06);

            border-left:
                3px solid #FC4C02;

            border-radius:
                8px;

            box-shadow:
                0 6px 18px rgba(0,0,0,0.22);
        }}


        .sidebar-brand-title {{
            color:
                #FFFFFF;

            font-size:
                21px;

            font-weight:
                800;

            letter-spacing:
                1.5px;

            line-height:
                1.1;
        }}


        .sidebar-brand-title span {{
            color:
                #FC4C02;
        }}


        .sidebar-brand-subtitle {{
            margin-top:
                8px;

            color:
                #747A84;

            font-size:
                9px;

            letter-spacing:
                1px;

            text-transform:
                uppercase;
        }}


        /* =====================================================
           SIDEBAR SECTION TITLE
           ===================================================== */

        .sidebar-section-title {{
            color:
                #737A84;

            font-size:
                10px;

            font-weight:
                700;

            letter-spacing:
                1.4px;

            text-transform:
                uppercase;

            margin-top:
                19px;

            margin-bottom:
                9px;
        }}


        /* =====================================================
           SIDEBAR STATUS
           ===================================================== */

        .sidebar-status-card {{
            background:
                linear-gradient(
                    145deg,
                    rgba(22,23,27,0.97),
                    rgba(8,9,11,0.97)
                );

            border:
                1px solid rgba(255,255,255,0.07);

            border-left:
                3px solid #FC4C02;

            border-radius:
                8px;

            padding:
                11px 12px;

            margin-bottom:
                8px;

            box-shadow:
                0 5px 16px rgba(0,0,0,0.18);
        }}


        .sidebar-status-row {{
            display:
                flex;

            align-items:
                center;

            gap:
                8px;

            margin-bottom:
                5px;
        }}


        .sidebar-dot {{
            width:
                7px;

            height:
                7px;

            background:
                #FC4C02;

            border-radius:
                50%;

            box-shadow:
                0 0 7px rgba(252,76,2,0.65);
        }}


        .sidebar-status-name {{
            color:
                #9CA3AD;

            font-size:
                10px;

            font-weight:
                700;

            letter-spacing:
                0.8px;

            text-transform:
                uppercase;
        }}


        .sidebar-status-value {{
            color:
                #FFFFFF;

            font-size:
                14px;

            font-weight:
                600;

            margin-left:
                15px;
        }}


        /* =====================================================
           SIDEBAR FITNESS INSIGHT
           ===================================================== */

        .sidebar-insight {{
            background:
                linear-gradient(
                    145deg,
                    rgba(252,76,2,0.09),
                    rgba(15,16,19,0.96)
                );

            border:
                1px solid rgba(252,76,2,0.22);

            border-radius:
                8px;

            padding:
                13px;

            margin-top:
                16px;

            box-shadow:
                0 0 15px rgba(252,76,2,0.05);
        }}


        .sidebar-insight-title {{
            color:
                #FC4C02;

            font-size:
                10px;

            font-weight:
                800;

            letter-spacing:
                1px;

            text-transform:
                uppercase;

            margin-bottom:
                7px;
        }}


        .sidebar-insight-text {{
            color:
                #9DA3AD;

            font-size:
                12px;

            line-height:
                1.5;
        }}


        /* =====================================================
           SIDEBAR FOOTER
           ===================================================== */

        .sidebar-footer {{
            color:
                #555B64;

            font-size:
                8px;

            letter-spacing:
                1px;

            text-transform:
                uppercase;

            text-align:
                center;

            margin-top:
                18px;

            padding-top:
                11px;

            border-top:
                1px solid rgba(255,255,255,0.05);
        }}


        /* =====================================================
           KPI CARDS
           ===================================================== */

        div[data-testid="stMetric"] {{
            background:
                linear-gradient(
                    145deg,
                    rgba(20,21,25,0.96),
                    rgba(8,9,12,0.96)
                );

            border:
                1px solid rgba(255,255,255,0.08);

            border-left:
                3px solid #FC4C02;

            border-radius:
                10px;

            padding:
                16px 18px;

            min-height:
                92px;

            box-shadow:
                0 0 18px rgba(252,76,2,0.08),
                inset 0 0 20px rgba(255,255,255,0.015);
        }}


        div[data-testid="stMetricLabel"] {{
            color:
                #9DA3AD !important;

            font-size:
                11px !important;

            font-weight:
                700 !important;

            letter-spacing:
                1.3px !important;
        }}


        div[data-testid="stMetricValue"] {{
            color:
                #FFFFFF !important;

            font-size:
                27px !important;

            font-weight:
                700 !important;
        }}


        /* =====================================================
           TABS
           ===================================================== */

        button[data-baseweb="tab"] {{
            font-family:
                'Rajdhani',
                sans-serif !important;
        }}


        button[data-baseweb="tab"][aria-selected="true"] {{
            color:
                #FC4C02 !important;

            border-bottom-color:
                #FC4C02 !important;
        }}


        /* =====================================================
           ALERTS
           ===================================================== */

        div[data-testid="stAlert"] {{
            border-left:
                3px solid #FC4C02;

            box-shadow:
                0 0 12px rgba(252,76,2,0.08);
        }}

        /* Expanders (Data Description / Limitations / Future Work dropdowns) */
        div[data-testid="stExpander"] {{
            background: linear-gradient(135deg, rgba(26, 31, 41, 0.85) 0%, rgba(18, 21, 28, 0.85) 100%);
            border: 1px solid rgba(252, 76, 2, 0.25);
            border-left: 4px solid #FC4C02;
            border-radius: 8px;
            box-shadow: 0 0 14px rgba(252, 76, 2, 0.10);
            margin-bottom: 14px;
        }}
        div[data-testid="stExpander"] summary {{
            font-family: 'Rajdhani', sans-serif !important;
            font-weight: 700 !important;
            font-size: 17px !important;
            color: #FAFAFA !important;
        }}
        div[data-testid="stExpander"] summary:hover {{
            color: #FC4C02 !important;
        }}
        div[data-testid="stExpanderDetails"] {{
            padding-top: 4px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def render_sidebar():

    st.sidebar.markdown(
        '<div class="sidebar-brand"><div class="sidebar-brand-title">FITNESS <span>ANALYTICS</span></div><div class="sidebar-brand-subtitle">Healthier Today • Stronger Tomorrow</div></div>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-section-title">System Status</div>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-status-card"><div class="sidebar-status-row"><div class="sidebar-dot"></div><div class="sidebar-status-name">Database</div></div><div class="sidebar-status-value">SQLite Connected</div></div>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-status-card"><div class="sidebar-status-row"><div class="sidebar-dot"></div><div class="sidebar-status-name">Analytics</div></div><div class="sidebar-status-value">30 SQL Queries Ready</div></div>',
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        '<div class="sidebar-status-card"><div class="sidebar-status-row"><div class="sidebar-dot"></div><div class="sidebar-status-name">Dashboard</div></div><div class="sidebar-status-value">10 Analysis Sections</div></div>',
        unsafe_allow_html=True
    )

    # =========================================================
    # FITNESS INSIGHT
    # =========================================================

    st.sidebar.markdown(
        '<div class="sidebar-insight"><div class="sidebar-insight-title">Fitness Insight</div><div class="sidebar-insight-text">Track activity, calories, sleep and heart rate to understand user fitness patterns.</div></div>',
        unsafe_allow_html=True
    )


    # =========================================================
    # FOOTER
    # =========================================================

    st.sidebar.markdown(
        '<div class="sidebar-footer">FITNESS DATA ANALYTICS</div>',
        unsafe_allow_html=True
    )

LOGO_PATH = Path(__file__).parent / "runner_logo.png"


def render_logo():
    """Places runner_logo.png at the top of the sidebar, above the page nav links,
    made bigger and centered (st.logo defaults to small + left-aligned)."""
    if LOGO_PATH.exists():
        st.logo(str(LOGO_PATH), size="large")

        st.markdown(
            """
            <style>
            [data-testid="stSidebarHeader"] {
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                padding-top: 30px !important;
                padding-bottom: 10px !important;
            }
            [data-testid="stSidebarHeader"] img,
            [data-testid="stLogo"],
            .stLogo {
                height: 90px !important;
                max-height: 90px !important;
                width: auto !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )