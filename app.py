import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import mannwhitneyu

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Retail Intelligence | EDA + Statistical Modeling",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PREMIUM CSS
# ============================================================

st.html("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.16), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,0.13), transparent 28%),
        radial-gradient(circle at 50% 90%, rgba(168,85,247,0.10), transparent 30%),
        #070b17;
    color: #f8fafc;
}

.main {
    background: transparent;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ---------- ANIMATED BACKGROUND ---------- */

.stApp::before {
    content: "";
    position: fixed;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: rgba(99,102,241,0.08);
    filter: blur(100px);
    top: 5%;
    left: -150px;
    z-index: -1;
    animation: floatOne 12s ease-in-out infinite alternate;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 450px;
    height: 450px;
    border-radius: 50%;
    background: rgba(14,165,233,0.07);
    filter: blur(100px);
    bottom: 0;
    right: -150px;
    z-index: -1;
    animation: floatTwo 15s ease-in-out infinite alternate;
}

@keyframes floatOne {
    from {
        transform: translate(0, 0);
    }
    to {
        transform: translate(100px, 80px);
    }
}

@keyframes floatTwo {
    from {
        transform: translate(0, 0);
    }
    to {
        transform: translate(-80px, -100px);
    }
}


/* ---------- HEADER ---------- */

.hero {
    position: relative;
    padding: 32px 36px;
    margin-bottom: 28px;
    border-radius: 24px;
    background:
        linear-gradient(
            135deg,
            rgba(30,41,59,0.92),
            rgba(15,23,42,0.82)
        );
    border: 1px solid rgba(148,163,184,0.18);
    box-shadow:
        0 25px 60px rgba(0,0,0,0.28),
        inset 0 1px 0 rgba(255,255,255,0.05);
    overflow: hidden;
}

.hero::before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    background: rgba(99,102,241,0.18);
    filter: blur(60px);
    right: -80px;
    top: -120px;
}

.hero::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: rgba(14,165,233,0.13);
    filter: blur(55px);
    left: -80px;
    bottom: -120px;
}

.hero-title {
    position: relative;
    z-index: 2;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 0;
    background: linear-gradient(
        90deg,
        #ffffff,
        #93c5fd,
        #c4b5fd
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    position: relative;
    z-index: 2;
    color: #94a3b8;
    font-size: 1.05rem;
    margin-top: 8px;
}

.hero-badge {
    position: relative;
    z-index: 2;
    display: inline-block;
    margin-top: 18px;
    padding: 7px 14px;
    border-radius: 999px;
    background: rgba(99,102,241,0.14);
    border: 1px solid rgba(129,140,248,0.28);
    color: #c7d2fe;
    font-size: 0.82rem;
    font-weight: 600;
}


/* ---------- SECTION TITLES ---------- */

.section-title {
    font-size: 1.55rem;
    font-weight: 750;
    color: #f8fafc;
    margin-top: 28px;
    margin-bottom: 16px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 0.92rem;
    margin-top: -10px;
    margin-bottom: 18px;
}


/* ---------- KPI CARDS ---------- */

.kpi-card {
    position: relative;
    min-height: 145px;
    padding: 22px;
    border-radius: 20px;
    background:
        linear-gradient(
            145deg,
            rgba(30,41,59,0.88),
            rgba(15,23,42,0.72)
        );
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow:
        0 15px 40px rgba(0,0,0,0.20),
        inset 0 1px 0 rgba(255,255,255,0.04);
    overflow: hidden;
    transition:
        transform 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-7px);
    border-color: rgba(129,140,248,0.45);
    box-shadow:
        0 20px 55px rgba(79,70,229,0.20),
        inset 0 1px 0 rgba(255,255,255,0.07);
}

.kpi-card::after {
    content: "";
    position: absolute;
    width: 130px;
    height: 130px;
    border-radius: 50%;
    right: -60px;
    bottom: -70px;
    background: rgba(99,102,241,0.12);
    filter: blur(20px);
}

.kpi-icon {
    font-size: 1.6rem;
    margin-bottom: 8px;
}

.kpi-label {
    color: #94a3b8;
    font-size: 0.82rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.kpi-value {
    color: #f8fafc;
    font-size: 1.75rem;
    font-weight: 800;
    margin-top: 6px;
}

.kpi-caption {
    color: #64748b;
    font-size: 0.76rem;
    margin-top: 6px;
}


/* ---------- GLASS PANEL ---------- */

.glass-panel {
    background: rgba(15,23,42,0.62);
    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 20px;
    padding: 22px;
    box-shadow:
        0 18px 45px rgba(0,0,0,0.18),
        inset 0 1px 0 rgba(255,255,255,0.04);
}


/* ---------- INSIGHT CARDS ---------- */

.insight {
    padding: 16px 18px;
    margin: 10px 0;
    border-radius: 14px;
    background: rgba(30,41,59,0.62);
    border: 1px solid rgba(148,163,184,0.12);
    border-left: 4px solid #818cf8;
    color: #cbd5e1;
    transition: transform 0.25s ease;
}

.insight:hover {
    transform: translateX(5px);
}


/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b1020 0%,
            #080d19 100%
        );
    border-right: 1px solid rgba(148,163,184,0.12);
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}


/* ---------- BUTTONS ---------- */

.stButton > button {
    border-radius: 10px;
    border: 1px solid rgba(129,140,248,0.3);
    background: rgba(99,102,241,0.12);
    color: #e0e7ff;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background: rgba(99,102,241,0.25);
    border-color: rgba(129,140,248,0.55);
    transform: translateY(-2px);
}


/* ---------- TABS ---------- */

button[data-baseweb="tab"] {
    color: #94a3b8;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #c7d2fe;
}


/* ---------- DATAFRAME ---------- */

div[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(148,163,184,0.12);
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #64748b;
    padding: 35px 0 10px 0;
    font-size: 0.82rem;
}

.footer strong {
    color: #a5b4fc;
}


/* ---------- MOBILE ---------- */

@media (max-width: 900px) {

    .hero-title {
        font-size: 2rem;
    }

    .hero {
        padding: 25px;
    }
}

</style>
""")


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    path = "data/cleaned/Online_Retail_Cleaned.csv"

    data = pd.read_csv(path)

    data["InvoiceDate"] = pd.to_datetime(
        data["InvoiceDate"],
        errors="coerce"
    )

    data["Quantity"] = pd.to_numeric(
        data["Quantity"],
        errors="coerce"
    )

    data["UnitPrice"] = pd.to_numeric(
        data["UnitPrice"],
        errors="coerce"
    )

    data["Revenue"] = (
        data["Quantity"] *
        data["UnitPrice"]
    )

    data["YearMonth"] = (
        data["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )

    data["DayOfWeek"] = (
        data["InvoiceDate"]
        .dt.day_name()
    )

    data["Hour"] = (
        data["InvoiceDate"]
        .dt.hour
    )

    return data


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "❌ Dataset not found.\n\n"
        "Expected:\n"
        "`data/cleaned/Online_Retail_Cleaned.csv`"
    )

    st.stop()

except Exception as error:

    st.error(f"❌ Error loading dataset: {error}")

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        font-size:1.35rem;
        font-weight:800;
        margin-bottom:4px;
    ">
    📊 Retail Intelligence
    </div>

    <div style="
        color:#64748b;
        font-size:0.82rem;
        margin-bottom:20px;
    ">
    Exploratory Data Analysis
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🎛️ Filters")

countries = sorted(
    df["Country"].dropna().unique()
)

selected_countries = st.sidebar.multiselect(
    "🌍 Countries",
    countries,
    default=[]
)

transaction_type = st.sidebar.radio(
    "🧾 Transaction Type",
    [
        "All Transactions",
        "Regular Sales",
        "Negative Transactions"
    ]
)

min_date = df["InvoiceDate"].min().date()
max_date = df["InvoiceDate"].max().date()

date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
        padding:12px;
        border-radius:12px;
        background:rgba(99,102,241,0.08);
        border:1px solid rgba(129,140,248,0.15);
        color:#94a3b8;
        font-size:0.78rem;
    ">
    <strong style="color:#c7d2fe;">
    Internship Project
    </strong><br><br>
    Junior Data Scientist Intern<br>
    Yuva Intern<br>
    Week 3 • Statistical Modeling<br><br>
    <span style="
        display:inline-block;
        padding:6px 10px;
        border-radius:8px;
        background:rgba(129,140,248,0.14);
        border:1px solid rgba(129,140,248,0.24);
        color:#c4b5fd;
        font-weight:700;
    ">👨‍💻 Anand Raj Yadav</span>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILTER DATA
# ============================================================

filtered = df.copy()

if selected_countries:

    filtered = filtered[
        filtered["Country"].isin(
            selected_countries
        )
    ]

if transaction_type == "Regular Sales":

    filtered = filtered[
        filtered["Quantity"] > 0
    ]

elif transaction_type == "Negative Transactions":

    filtered = filtered[
        filtered["Quantity"] < 0
    ]

if (
    isinstance(date_range, tuple)
    and len(date_range) == 2
):

    start_date, end_date = date_range

    filtered = filtered[
        (
            filtered["InvoiceDate"].dt.date
            >= start_date
        )
        &
        (
            filtered["InvoiceDate"].dt.date
            <= end_date
        )
    ]


# ============================================================
# HERO
# ============================================================

st.html("""
    <div class="hero">

        <div class="hero-title">
            📊 Online Retail Intelligence
        </div>

        <div class="hero-subtitle">
            Interactive Retail Intelligence Dashboard
            • EDA • Statistical Modeling • Hypothesis Testing • Business Insights
        </div>

        <div class="hero-badge">
            🚀 Junior Data Scientist Internship • Week 3 • Statistical Modeling
        </div>

        <div style="
            position:relative;
            z-index:2;
            display:inline-flex;
            align-items:center;
            gap:8px;
            margin-top:12px;
            padding:8px 15px;
            border-radius:999px;
            background:linear-gradient(90deg, rgba(99,102,241,0.20), rgba(14,165,233,0.16));
            border:1px solid rgba(129,140,248,0.34);
            color:#e0e7ff;
            font-size:0.86rem;
            font-weight:700;
            box-shadow:0 8px 25px rgba(79,70,229,0.12);
        ">
            👨‍💻 Developed by <span style="color:#c4b5fd;">Anand Raj Yadav</span>
        </div>

    </div>
    """)


# ============================================================
# KPI CALCULATIONS
# ============================================================

records = len(filtered)

revenue = filtered["Revenue"].sum()

regular = filtered.loc[
    filtered["Quantity"] > 0,
    "Revenue"
].sum()

negative = filtered.loc[
    filtered["Quantity"] < 0,
    "Revenue"
].sum()

negative_count = (
    filtered["Quantity"] < 0
).sum()

products = filtered["StockCode"].nunique()

customers = filtered["CustomerID"].nunique()

orders = filtered["InvoiceNo"].nunique()

if regular != 0:

    negative_ratio = (
        abs(negative) /
        abs(regular)
    ) * 100

else:

    negative_ratio = 0


# ============================================================
# KPI CARDS
# ============================================================

st.html('<div class="section-title">⚡ Performance Snapshot</div>')

c1, c2, c3, c4, c5 = st.columns(5)

cards = [

    (
        c1,
        "📦",
        "Records",
        f"{records:,}",
        "Filtered transactions"
    ),

    (
        c2,
        "💰",
        "Revenue",
        f"£{revenue:,.0f}",
        "Recorded revenue"
    ),

    (
        c3,
        "🧾",
        "Orders",
        f"{orders:,}",
        "Unique invoices"
    ),

    (
        c4,
        "👥",
        "Customers",
        f"{customers:,}",
        "Identified customers"
    ),

    (
        c5,
        "↩️",
        "Negative Txns",
        f"{negative_count:,}",
        f"{negative_ratio:.2f}% revenue impact"
    )
]

for container, icon, label, value, caption in cards:

    with container:

        st.html(f"""
            <div class="kpi-card">

                <div class="kpi-icon">
                    {icon}
                </div>

                <div class="kpi-label">
                    {label}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

                <div class="kpi-caption">
                    {caption}
                </div>

            </div>
            """)


# ============================================================
# NAVIGATION TABS
# ============================================================

st.html("""
<div style="
    margin:6px 0 18px 0;
    padding:12px 18px;
    border-radius:14px;
    background:rgba(15,23,42,0.58);
    border:1px solid rgba(148,163,184,0.13);
    box-shadow:inset 0 1px 0 rgba(255,255,255,0.04);
    color:#94a3b8;
    font-size:0.88rem;
">
    <span style="color:#c4b5fd;font-weight:800;">ANALYST</span>
    &nbsp;•&nbsp; Anand Raj Yadav
    &nbsp;&nbsp;|&nbsp;&nbsp;
    <span style="color:#cbd5e1;">Junior Data Scientist Intern</span>
</div>
""")

tabs = st.tabs(
    [
        "🏠 Overview",
        "📈 Sales",
        "🌍 Geography",
        "📦 Products",
        "👥 Customers",
        "↩️ Returns",
        "🧪 Statistics",
        "📊 Week 3 Modeling",
        "🔎 Explorer"
    ]
)


# ============================================================
# OVERVIEW
# ============================================================

with tabs[0]:

    st.html('<div class="section-title">📌 Business Overview</div>')

    a, b = st.columns(2)

    with a:

        st.html('<div class="glass-panel">')

        st.markdown("### 💰 Revenue Structure")

        revenue_values = pd.DataFrame(
            {
                "Type": [
                    "Regular Sales",
                    "Negative Transactions"
                ],
                "Revenue": [
                    abs(regular),
                    abs(negative)
                ]
            }
        )

        fig = px.pie(
            revenue_values,
            names="Type",
            values="Revenue",
            hole=0.65
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            margin=dict(
                l=10,
                r=10,
                t=30,
                b=10
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with b:

        st.html('<div class="glass-panel">')

        st.markdown("### 🧠 Quick Insights")

        overview_insights = [

            f"Dataset contains **{records:,} records**.",

            f"Regular sales generated approximately "
            f"**£{regular:,.2f}**.",

            f"Negative transactions: **{negative_count:,}**.",

            f"Negative transactions represent approximately "
            f"**{negative_ratio:.2f}%** of regular-sales revenue "
            f"by absolute value.",

            "Outliers were investigated rather than blindly removed.",

            "Customer analysis uses records with available CustomerID."

        ]

        for item in overview_insights:

            st.html(f'<div class="insight">💡 {item}</div>')

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# SALES ANALYTICS
# ============================================================

with tabs[1]:

    st.html('<div class="section-title">📈 Sales Analytics</div>')

    sales_df = filtered[
        filtered["Quantity"] > 0
    ]

    monthly = (
        sales_df
        .groupby("YearMonth", as_index=False)
        ["Revenue"]
        .sum()
    )

    fig_month = px.area(
        monthly,
        x="YearMonth",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig_month.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

    day_col, hour_col = st.columns(2)

    with day_col:

        day_order = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        day_data = (
            sales_df
            .groupby("DayOfWeek")
            ["Revenue"]
            .sum()
            .reindex(day_order)
            .reset_index()
        )

        fig_day = px.bar(
            day_data,
            x="DayOfWeek",
            y="Revenue",
            title="Revenue by Day"
        )

        fig_day.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig_day,
            use_container_width=True
        )

    with hour_col:

        hour_data = (
            sales_df
            .groupby("Hour")
            ["Revenue"]
            .sum()
            .reset_index()
        )

        fig_hour = px.line(
            hour_data,
            x="Hour",
            y="Revenue",
            markers=True,
            title="Revenue by Hour"
        )

        fig_hour.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig_hour,
            use_container_width=True
        )


# ============================================================
# GEOGRAPHY
# ============================================================

with tabs[2]:

    st.html('<div class="section-title">🌍 Geographic Analysis</div>')

    country_data = (
        filtered[
            filtered["Quantity"] > 0
        ]
        .groupby("Country", as_index=False)
        ["Revenue"]
        .sum()
        .sort_values(
            "Revenue",
            ascending=False
        )
    )

    top_country = country_data.head(15)

    fig_country = px.bar(
        top_country.sort_values("Revenue"),
        x="Revenue",
        y="Country",
        orientation="h",
        title="Top Countries by Revenue"
    )

    fig_country.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_country,
        use_container_width=True
    )

    if not country_data.empty:

        top = country_data.iloc[0]

        st.html(f"""
            <div class="insight">
            🌍 Highest revenue contribution:
            <strong>{top["Country"]}</strong>
            with approximately
            <strong>£{top["Revenue"]:,.2f}</strong>.
            </div>
            """)


# ============================================================
# PRODUCT ANALYSIS
# ============================================================

with tabs[3]:

    st.html('<div class="section-title">📦 Product Intelligence</div>')

    product_data = (
        filtered[
            filtered["Quantity"] > 0
        ]
        .groupby("Description", as_index=False)
        ["Revenue"]
        .sum()
        .sort_values(
            "Revenue",
            ascending=False
        )
        .head(15)
    )

    fig_product = px.bar(
        product_data.sort_values("Revenue"),
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 15 Products by Revenue"
    )

    fig_product.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )

    if not product_data.empty:

        top_product = product_data.iloc[-1]

        st.html(f"""
            <div class="insight">
            🏆 Highest-revenue product line:
            <strong>{top_product["Description"]}</strong>
            with approximately
            <strong>£{top_product["Revenue"]:,.2f}</strong>.
            </div>
            """)


# ============================================================
# CUSTOMER ANALYSIS
# ============================================================

with tabs[4]:

    st.html('<div class="section-title">👥 Customer Intelligence</div>')

    customer_data = filtered[
        (filtered["Quantity"] > 0)
        &
        (filtered["CustomerID"].notna())
    ].copy()

    if not customer_data.empty:

        aov = (
            customer_data["Revenue"].sum()
            /
            customer_data["InvoiceNo"].nunique()
        )

        customer_summary = (
            customer_data
            .groupby("CustomerID")
            .agg(
                Revenue=("Revenue", "sum"),
                Orders=("InvoiceNo", "nunique")
            )
            .reset_index()
        )

        customer_summary["AOV"] = (
            customer_summary["Revenue"]
            /
            customer_summary["Orders"]
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Average Order Value",
                f"£{aov:,.2f}"
            )

        with c2:

            st.metric(
                "Identified Customers",
                f"{len(customer_summary):,}"
            )

        with c3:

            st.metric(
                "Customer Revenue",
                f"£{customer_data['Revenue'].sum():,.0f}"
            )

        top_customers = (
            customer_summary
            .sort_values(
                "Revenue",
                ascending=False
            )
            .head(10)
        )

        fig_customer = px.bar(
            top_customers.sort_values("Revenue"),
            x="Revenue",
            y="CustomerID",
            orientation="h",
            title="Top 10 Customers by Revenue"
        )

        fig_customer.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig_customer,
            use_container_width=True
        )


# ============================================================
# RETURNS ANALYSIS
# ============================================================

with tabs[5]:

    st.html('<div class="section-title">↩️ Returns & Negative Transactions</div>')

    returns = filtered[
        filtered["Quantity"] < 0
    ].copy()

    if not returns.empty:

        r1, r2, r3 = st.columns(3)

        with r1:

            st.metric(
                "Negative Transactions",
                f"{len(returns):,}"
            )

        with r2:

            st.metric(
                "Negative Quantity",
                f"{abs(returns['Quantity'].sum()):,.0f}"
            )

        with r3:

            st.metric(
                "Revenue Impact",
                f"£{abs(returns['Revenue'].sum()):,.2f}"
            )

        country_returns = (
            returns
            .groupby("Country")
            .size()
            .reset_index(
                name="Transactions"
            )
            .sort_values(
                "Transactions",
                ascending=False
            )
            .head(15)
        )

        fig_returns = px.bar(
            country_returns.sort_values(
                "Transactions"
            ),
            x="Transactions",
            y="Country",
            orientation="h",
            title="Negative Transactions by Country"
        )

        fig_returns.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig_returns,
            use_container_width=True
        )

    else:

        st.info(
            "No negative transactions found "
            "for the selected filters."
        )


# ============================================================
# STATISTICAL ANALYSIS
# ============================================================

with tabs[6]:

    st.html('<div class="section-title">🧪 Statistical Analysis</div>')

    numeric = filtered[
        [
            "Quantity",
            "UnitPrice",
            "Revenue"
        ]
    ].dropna()

    if not numeric.empty:

        st.markdown("### 🔗 Correlation Matrix")

        correlation = numeric.corr()

        fig_corr = px.imshow(
            correlation,
            text_auto=".2f",
            aspect="auto"
        )

        fig_corr.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig_corr,
            use_container_width=True
        )

        st.caption(
            "Revenue is mathematically derived from Quantity × UnitPrice; "
            "therefore correlation with these variables is not causal evidence."
        )

    st.markdown("### 📦 IQR Outlier Analysis")

    outlier_cols = [
        "Quantity",
        "UnitPrice",
        "Revenue"
    ]

    outlier_results = []

    for column in outlier_cols:

        values = filtered[column].dropna()

        if len(values) == 0:
            continue

        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        count = (
            (values < lower)
            |
            (values > upper)
        ).sum()

        outlier_results.append(
            {
                "Variable": column,
                "Q1": q1,
                "Q3": q3,
                "Lower Bound": lower,
                "Upper Bound": upper,
                "Outliers": count
            }
        )

    st.dataframe(
        pd.DataFrame(outlier_results),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 🧪 Mann–Whitney U Test")

    regular_data = filtered[
        filtered["Quantity"] > 0
    ]

    country_counts = (
        regular_data["Country"]
        .value_counts()
    )

    if len(country_counts) >= 2:

        country_1 = country_counts.index[0]
        country_2 = country_counts.index[1]

        group_1 = regular_data[
            regular_data["Country"] == country_1
        ]["Revenue"].dropna()

        group_2 = regular_data[
            regular_data["Country"] == country_2
        ]["Revenue"].dropna()

        statistic, p_value = mannwhitneyu(
            group_1,
            group_2,
            alternative="two-sided"
        )

        median_1 = group_1.median()
        median_2 = group_2.median()

        effect_size = (
            2 * statistic /
            (len(group_1) * len(group_2))
        ) - 1

        t1, t2, t3, t4 = st.columns(4)

        with t1:
            st.metric(
                "Group 1",
                country_1
            )

        with t2:
            st.metric(
                "Group 2",
                country_2
            )

        with t3:
            st.metric(
                "p-value",
                f"{p_value:.6f}"
            )

        with t4:
            st.metric(
                "Effect Size",
                f"{effect_size:.4f}"
            )

        st.html(f"""
            <div class="insight">

            <strong>Median Order Value</strong><br><br>

            {country_1}: £{median_1:,.2f}<br>
            {country_2}: £{median_2:,.2f}<br><br>

            The test evaluates whether the two order-value
            distributions differ statistically.

            </div>
            """)



# ============================================================
# WEEK 3 — STATISTICAL MODELING & HYPOTHESIS TESTING
# ============================================================

with tabs[7]:

    st.html('<div class="section-title">📊 Week 3 • Statistical Modeling & Hypothesis Testing</div>')
    st.html(
        '<div class="section-subtitle">'
        'Invoice-level OLS modeling, robust statistical inference, diagnostics, '
        'hypothesis testing and sensitivity analysis.'
        '</div>'
    )

    # Final validated Week 3 results from the statistical modeling notebook/report.
    MODEL_N = 19960
    MODEL_R2 = 0.285469
    MODEL_ADJ_R2 = 0.284860
    MODEL_MAE = 0.712313
    MODEL_RMSE = 1.019302
    MODEL_P = "< 0.001"
    BP_P = "< 0.001"
    SENS_N = 19259
    REMOVED = 701
    SENS_R2 = 0.413878

    h1_p = 0.08383
    h2_p = 4.235e-43
    h3_p = 0.16141

    # -----------------------------
    # Model KPI cards
    # -----------------------------
    st.html('<div class="section-title">🎯 Model Performance</div>')

    m1, m2, m3, m4, m5 = st.columns(5)

    model_cards = [
        (m1, "📊", "Observations", f"{MODEL_N:,}", "Invoice-level orders"),
        (m2, "R²", "R²", f"{MODEL_R2:.4f}", "Variance explained"),
        (m3, "📐", "Adjusted R²", f"{MODEL_ADJ_R2:.4f}", "Adjusted for predictors"),
        (m4, "📉", "MAE", f"{MODEL_MAE:.4f}", "Log scale"),
        (m5, "📏", "RMSE", f"{MODEL_RMSE:.4f}", "Log scale"),
    ]

    for container, icon, label, value, caption in model_cards:
        with container:
            st.html(f"""
                <div class="kpi-card">
                    <div class="kpi-icon">{icon}</div>
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-caption">{caption}</div>
                </div>
            """)

    st.markdown("")

    # -----------------------------
    # Research question
    # -----------------------------
    st.html('<div class="section-title">🔬 Research Question</div>')
    st.html("""
        <div class="glass-panel">
            <div class="insight">
                <strong>Research Question:</strong><br>
                Which transaction, product-mix and temporal characteristics are
                significantly associated with invoice-level order value?
            </div>
            <div class="insight">
                <strong>Primary Target:</strong> LogOrderValue = log(1 + OrderValue)
                &nbsp; • &nbsp;
                <strong>Model:</strong> Ordinary Least Squares (OLS)
                &nbsp; • &nbsp;
                <strong>Inference:</strong> HC3 robust standard errors
            </div>
        </div>
    """)

    # -----------------------------
    # Hypotheses
    # -----------------------------
    st.html('<div class="section-title">🧪 Hypothesis Testing</div>')

    hypothesis_df = pd.DataFrame([
        {
            "Hypothesis": "H1 — Total Quantity",
            "p-value": h1_p,
            "Decision": "Fail to Reject H₀",
            "Interpretation": "Insufficient evidence of a significant association at 5%."
        },
        {
            "Hypothesis": "H2 — Unique Products",
            "p-value": h2_p,
            "Decision": "Reject H₀",
            "Interpretation": "Strong evidence of a significant association with order value."
        },
        {
            "Hypothesis": "H3 — Country",
            "p-value": h3_p,
            "Decision": "Fail to Reject H₀",
            "Interpretation": "Country is not statistically significant after controls."
        }
    ])

    h1, h2, h3 = st.columns(3)

    cards = [
        (h1, "H1", "Total Quantity", h1_p, "Fail to Reject H₀"),
        (h2, "H2", "Unique Products", h2_p, "Reject H₀"),
        (h3, "H3", "Country", h3_p, "Fail to Reject H₀")
    ]

    for col, h, variable, p, decision in cards:
        with col:
            decision_icon = "✅" if p < 0.05 else "⚪"
            p_display = f"{p:.3e}" if p < 0.001 else f"{p:.5f}"
            st.html(f"""
                <div class="glass-panel">
                    <div style="font-size:1.5rem;font-weight:800;color:#c4b5fd;">{h}</div>
                    <div style="font-size:1.05rem;font-weight:700;margin-top:5px;">{variable}</div>
                    <div style="color:#94a3b8;margin-top:12px;">p-value</div>
                    <div style="font-size:1.45rem;font-weight:800;margin-top:3px;">{p_display}</div>
                    <div class="insight" style="margin-top:14px;">
                        {decision_icon} <strong>{decision}</strong>
                    </div>
                </div>
            """)

    st.dataframe(
        hypothesis_df.assign(
            **{"p-value": hypothesis_df["p-value"].map(
                lambda x: f"{x:.3e}" if x < 0.001 else f"{x:.5f}"
            )}
        ),
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------
    # Model interpretation
    # -----------------------------
    st.html('<div class="section-title">📈 Statistical Interpretation</div>')

    st.html("""
        <div class="glass-panel">
            <div class="insight">
                <strong>Unique Products:</strong>
                This predictor showed extremely strong statistical evidence of an
                association with order value. More diverse product baskets are
                therefore an important signal for understanding high-value orders.
                This is an association, not proof of causality.
            </div>

            <div class="insight">
                <strong>Total Quantity:</strong>
                The p-value of 0.08383 is above the 5% threshold. The analysis
                therefore does not provide sufficient evidence to reject the null
                hypothesis at α = 0.05.
            </div>

            <div class="insight">
                <strong>Country:</strong>
                The p-value of 0.16141 indicates insufficient evidence that the
                country grouping is independently associated with order value
                after the other model variables are controlled.
            </div>
        </div>
    """)

    # -----------------------------
    # Model metrics / diagnostics
    # -----------------------------
    d1, d2 = st.columns(2)

    with d1:
        st.html('<div class="section-title">🩺 Diagnostic Checks</div>')
        diagnostics = pd.DataFrame([
            ["Overall model", MODEL_P, "Statistically significant"],
            ["Breusch–Pagan test", BP_P, "Heteroscedasticity detected"],
            ["Robust inference", "HC3", "Used for coefficient inference"],
            ["Primary target", "LogOrderValue", "Log-transformed order value"],
        ], columns=["Check", "Result", "Interpretation"])

        st.dataframe(
            diagnostics,
            use_container_width=True,
            hide_index=True
        )

    with d2:
        st.html('<div class="section-title">🧩 Predictors</div>')
        predictors = pd.DataFrame({
            "Feature": [
                "TotalQuantity",
                "UniqueProducts",
                "AvgUnitPrice",
                "Hour",
                "DayOfWeek",
                "Month",
                "IsWeekend",
                "CountryGroup"
            ],
            "Role": [
                "Transaction quantity",
                "Product diversity",
                "Average unit price",
                "Purchase hour",
                "Day-of-week effect",
                "Seasonality",
                "Weekend indicator",
                "Country grouping"
            ]
        })
        st.dataframe(
            predictors,
            use_container_width=True,
            hide_index=True
        )

    # -----------------------------
    # R² comparison
    # -----------------------------
    st.html('<div class="section-title">🔍 Sensitivity Analysis</div>')

    sensitivity_df = pd.DataFrame({
        "Model": ["Full Model", "Sensitivity Model"],
        "Observations": [MODEL_N, SENS_N],
        "Removed": [0, REMOVED],
        "R²": [MODEL_R2, SENS_R2]
    })

    fig_sens = px.bar(
        sensitivity_df,
        x="Model",
        y="R²",
        text="R²",
        title="Model Fit Before vs After Influence Screening"
    )
    fig_sens.update_traces(texttemplate="%{text:.4f}", textposition="outside")
    fig_sens.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(range=[0, max(SENS_R2 * 1.18, 0.5)])
    )
    st.plotly_chart(fig_sens, use_container_width=True)

    s1, s2, s3 = st.columns(3)
    with s1:
        st.metric("Full Model R²", f"{MODEL_R2:.4f}")
    with s2:
        st.metric("Sensitivity R²", f"{SENS_R2:.4f}")
    with s3:
        st.metric("Potentially Influential", f"{REMOVED:,}")

    st.html("""
        <div class="insight">
            ⚠️ The increase in R² after influence screening shows that unusual
            observations materially affect model fit. These observations should
            be investigated as possible bulk orders, unusually high-value orders,
            or other special transaction segments rather than being automatically
            treated as errors.
        </div>
    """)

    # -----------------------------
    # Business implications
    # -----------------------------
    st.html('<div class="section-title">💼 Business Implications</div>')

    implications = [
        "🛒 <strong>Product diversity matters:</strong> Unique Products is the strongest statistically supported predictor in this analysis, suggesting that cross-selling and basket-building strategies deserve attention.",
        "🎯 <strong>Recommendation systems:</strong> Product combinations and basket diversity can be useful inputs for personalized recommendations and bundle strategies.",
        "📦 <strong>Quantity needs deeper modeling:</strong> Total Quantity was not significant at 5%, so nonlinear effects, product mix and interaction effects may be more informative than quantity alone.",
        "🌍 <strong>Country is not independently significant:</strong> Geographic differences should not be interpreted from country alone once other transaction characteristics are controlled.",
        "🔎 <strong>Influential orders matter:</strong> The sensitivity analysis indicates that a small number of unusual observations can substantially change model fit and should be investigated as a separate business segment."
    ]

    for item in implications:
        st.html(f'<div class="insight">{item}</div>')

    # -----------------------------
    # Limitations / future work
    # -----------------------------
    l1, l2 = st.columns(2)

    with l1:
        st.html('<div class="section-title">⚠️ Assumptions & Limitations</div>')
        st.html("""
            <div class="glass-panel">
                <div class="insight">The analysis is observational and therefore does not establish causality.</div>
                <div class="insight">Heteroscedasticity was detected, so HC3 robust standard errors were used.</div>
                <div class="insight">Country categories were grouped to reduce sparse-category instability.</div>
                <div class="insight">CustomerID was not used as a raw numeric predictor.</div>
                <div class="insight">Negative quantities were excluded from the primary positive-sales order-value model because they may represent returns, cancellations or reversals.</div>
            </div>
        """)

    with l2:
        st.html('<div class="section-title">🚀 Future Improvements</div>')
        st.html("""
            <div class="glass-panel">
                <div class="insight">Add product categories, promotions and discount-related variables.</div>
                <div class="insight">Test nonlinear and interaction effects.</div>
                <div class="insight">Compare Ridge, Lasso and tree-based models.</div>
                <div class="insight">Use train-test splits and cross-validation for predictive evaluation.</div>
                <div class="insight">Explore RFM/customer-level and mixed-effects modeling.</div>
                <div class="insight">Investigate influential orders as meaningful business segments.</div>
            </div>
        """)

    # -----------------------------
    # Report download
    # -----------------------------
    st.html('<div class="section-title">📄 Week 3 Deliverable</div>')

    report_path = "report/Week_3_Statistical_Modeling_Report.pdf"

    try:
        with open(report_path, "rb") as report_file:
            st.download_button(
                label="⬇️ Download Week 3 Statistical Modeling Report",
                data=report_file.read(),
                file_name="Week_3_Statistical_Modeling_Report.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.info(
            "Week 3 PDF report is not available in the deployed repository yet. "
            "The statistical results above are still available."
        )


# ============================================================
# DATA EXPLORER
# ============================================================

with tabs[8]:

    st.html('<div class="section-title">🔎 Interactive Data Explorer</div>')

    st.html('<div class="section-subtitle">'
        'Explore the filtered dataset directly.'
        '</div>')

    st.dataframe(
        filtered,
        use_container_width=True,
        height=600
    )

    csv = filtered.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Dataset",
        data=csv,
        file_name="filtered_online_retail.csv",
        mime="text/csv"
    )


# ============================================================
# FOOTER
# ============================================================

st.html("""
    <div class="footer">

        <strong>Retail Intelligence Dashboard</strong><br><br>

        <span style="color:#c4b5fd;font-size:0.95rem;font-weight:800;">
            👨‍💻 Developed by Anand Raj Yadav
        </span><br>

        Built with Python • Pandas • Plotly • SciPy • Streamlit<br>

        Junior Data Scientist Internship • Yuva Intern • Week 3 Statistical Modeling

    </div>
    """)