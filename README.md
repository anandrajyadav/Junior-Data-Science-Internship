<div align="center">

# 🚀 Junior Data Science Internship

### 📊 Junior Data Scientist Intern — Yuva Intern

**A 6-Week Practical Data Science Journey**

🧹 Data Cleaning • 📊 EDA • 📐 Statistics • 🤖 Machine Learning • 💡 Business Insights

---

### 🟢 Internship Status: ACTIVE

**September 2026 — November 2026**

</div>

---

# 🏢 Internship Overview

| 🔹 Category | 📌 Details |
|---|---|
| **Organization** | Yuva Intern |
| **Role** | Junior Data Scientist Intern |
| **Duration** | 25 September 2026 – 06 November 2026 |
| **Program** | 6-Week Data Science Internship |
| **Primary Domain** | Data Science & Analytics |
| **Current Progress** | 🟢 Week 2 Completed |
| **Repository Status** | 🟢 Active |

---

# 🎯 About This Repository

This repository documents my complete **Junior Data Science Internship journey with Yuva Intern**.

The objective of this internship is to gain practical experience across the complete data science workflow — from raw data preparation and exploratory analysis to statistical reasoning, machine learning, model evaluation, and business-oriented insights.

The project follows a structured approach:

<div align="center">

**Raw Data**  
↓  
**Data Cleaning & Preprocessing**  
↓  
**Exploratory Data Analysis**  
↓  
**Statistical Analysis**  
↓  
**Machine Learning**  
↓  
**Model Evaluation**  
↓  
**Business Insights**

</div>

Each weekly task is documented through reproducible notebooks, reports, analysis, and supporting project files.

---

# 🗺️ Internship Roadmap

| Week | Focus Area | Status |
|---|---|---|
| 🧹 **Week 1** | Data Gathering, Cleaning & Preprocessing | ✅ Completed |
| 📊 **Week 2** | Exploratory Data Analysis | ✅ Completed |
| ⚙️ **Week 3** | Advanced Analysis / Feature Engineering | 🔜 Upcoming |
| 🤖 **Week 4** | Machine Learning | 🔜 Upcoming |
| 📈 **Week 5** | Model Evaluation & Improvement | 🔜 Upcoming |
| 🏆 **Week 6** | Final Project & Business Insights | 🔜 Upcoming |

### 📈 Current Progress

```text
Week 1  ████████████████████  100% ✅
Week 2  ████████████████████  100% ✅
Week 3  ░░░░░░░░░░░░░░░░░░░░    0% 🔜
Week 4  ░░░░░░░░░░░░░░░░░░░░    0% 🔜
Week 5  ░░░░░░░░░░░░░░░░░░░░    0% 🔜
Week 6  ░░░░░░░░░░░░░░░░░░░░    0% 🔜
```

---

# 🛠️ Technology Stack

### 💻 Programming

`Python`

### 📦 Data Analysis

`Pandas` `NumPy`

### 📊 Data Visualization

`Matplotlib` `Seaborn`

### 📐 Statistics

`SciPy` `Descriptive Statistics` `IQR` `Mann–Whitney U Test`

### 📓 Development

`Jupyter Notebook` `VS Code`

### 🔧 Version Control

`Git` `GitHub`

---

# 📁 Repository Structure

```text
Junior-Data-Science-Internship/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── Online Retail.xlsx
│   │
│   └── 📂 cleaned/
│       └── Online_Retail_Cleaned.csv
│
├── 📂 notebooks/
│   ├── Week_1_Data_Cleaning.ipynb
│   └── Week_2_EDA.ipynb
│
├── 📂 report/
│   ├── Week_1_Data_Cleaning_Report.pdf
│   └── Week_2_EDA_Report.pdf
│
├── 📂 src/
│   └── data_cleaning.py
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

# 🧹 WEEK 1 — Data Gathering, Cleaning & Preprocessing

## 🎯 Objective

The objective of Week 1 was to collect a publicly available retail dataset, understand its structure, identify data-quality issues, clean and preprocess the data, and prepare a reliable dataset for further analysis.

---

## 📊 Dataset

The project uses the **Online Retail dataset**, containing transaction-level retail information.

### Main Columns

- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

---

## 🧹 Data Cleaning Performed

The following preprocessing steps were completed:

1. Initial dataset exploration
2. Missing-value analysis
3. Duplicate detection and removal
4. Data-type validation and conversion
5. Missing product descriptions handled using `Unknown Product`
6. Invalid `UnitPrice` values identified and removed
7. Negative quantities investigated and retained
8. Statistical outliers investigated using the IQR method
9. Final data-quality validation
10. Cleaned dataset exported as CSV

---

## 📊 Week 1 Dataset Transformation

| Metric | Result |
|---|---:|
| Original records | **541,909** |
| Duplicate rows removed | **5,263** |
| Invalid UnitPrice records removed | **2,517** |
| Final cleaned records | **534,129** |
| Final columns | **8** |
| Remaining duplicates | **0** |

---

## 🔍 Data-Handling Decisions

### 🔄 Negative Quantities

Negative quantities were **not automatically removed**.

They may represent:

- Returns
- Cancellations
- Credit transactions
- Transaction reversals

Removing them without sufficient evidence could remove meaningful business information.

Therefore, negative quantities were retained and analyzed separately during Week 2.

---

### 👤 Missing CustomerID

Missing `CustomerID` values were retained because reliable customer identities cannot be inferred from the available transaction fields.

---

### 📦 Outliers

Outliers were investigated using the **Interquartile Range (IQR)** method.

They were not automatically removed because unusual retail transactions may represent:

- Bulk purchases
- High-value orders
- Legitimate business activity

---

# 📊 WEEK 2 — Exploratory Data Analysis

## 🎯 Objective

Week 2 focused on performing comprehensive **Exploratory Data Analysis (EDA)** on the cleaned Online Retail dataset prepared during Week 1.

The analysis focused on:

- Distributions
- Relationships
- Trends
- Customer behaviour
- Product performance
- Country-level sales
- Negative transactions
- Outliers
- Statistical differences between groups

---

# 🔬 EDA Workflow

```text
Cleaned Dataset
      │
      ├── Descriptive Statistics
      │
      ├── Revenue Analysis
      │
      ├── Negative Quantity Analysis
      │
      ├── Outlier Detection
      │
      ├── Distribution Analysis
      │
      ├── Correlation Analysis
      │
      ├── Scatter Plot Analysis
      │
      ├── Time-Based Analysis
      │
      ├── Product Analysis
      │
      ├── Country Analysis
      │
      ├── Customer Analysis
      │
      ├── AOV Analysis
      │
      └── Hypothesis Testing
```

---

# 📊 Week 2 Dataset

| Metric | Value |
|---|---:|
| Records analyzed | **534,129** |
| Duplicate rows | **0** |
| Original numerical variables | `Quantity`, `UnitPrice` |
| Derived variable | `Revenue` |
| Customers with available CustomerID | **4,338** |

---

# 💰 Revenue Analysis

Revenue was calculated as:

```text
Revenue = Quantity × UnitPrice
```

### Results

| Metric | Value |
|---|---:|
| Regular positive-quantity sales revenue | **10,642,110.80** |
| Negative transaction impact | **-893,979.73** |
| Net recorded revenue | **9,748,131.07** |

### 🔎 Interpretation

Negative transactions were analyzed separately because they may represent returns, cancellations, credits, or other reversals.

Separating these observations prevents regular sales analysis from mixing normal sales activity with potential reversal activity.

---

# 🔄 Negative Quantity Analysis

| Metric | Result |
|---|---:|
| Negative transactions | **9,251** |
| Percentage of dataset | **1.73%** |
| Total negative quantity | **-275,560** |
| Revenue impact | **-893,979.73** |

### 🧠 Analytical Decision

```text
Negative Transactions
        ↓
      Retain
        ↓
Analyze Separately
        ↓
Compare With Regular Sales
```

Negative quantities were retained because the dataset does not provide enough information to definitively classify every negative transaction.

---

# 📦 Product-Level Analysis

The highest-revenue dataset line item was:

### 🥇 DOTCOM POSTAGE

**Recorded Revenue: 206,248.77**

> `DOTCOM POSTAGE` is a postage/service-related line item rather than a conventional physical product. Therefore, it should not automatically be interpreted as the highest-demand physical product.

This distinction is important for accurate business interpretation.

---

# 🌍 Country-Level Analysis

The country with the highest recorded regular-sales revenue in the analysis was:

### 🇬🇧 United Kingdom

**Revenue: 9,001,744.09**

This describes the observed dataset and does not by itself establish profitability, market potential, or future performance.

---

# 👥 Customer Analysis

Customer analysis was restricted to records containing a valid `CustomerID`.

| Metric | Result |
|---|---:|
| Identified customers | **4,338** |
| Identified-customer orders | **18,532** |
| Identified-customer revenue | **8,887,208.89** |
| Overall invoice-level AOV | **479.56** |

### 📌 AOV Formula

```text
AOV = Total Customer Revenue / Total Orders
```

AOV was calculated at the **invoice/order level**, rather than treating every transaction line as a separate order.

---

# 📦 Outlier Analysis

The IQR method was used to investigate statistical outliers in:

- `Quantity`
- `UnitPrice`
- `Revenue`

### Important Principle

```text
Statistical Outlier
        ≠
Data Error
```

An extreme observation may represent:

- Bulk purchasing
- High-value transactions
- Expensive products
- Legitimate business activity

Therefore, outliers were investigated rather than automatically deleted.

---

# 📈 Distribution & Relationship Analysis

The following visual analyses were performed:

- Histograms
- Box plots
- Scatter plots
- Correlation heatmap

Relationships investigated included:

- Quantity ↔ UnitPrice
- Quantity ↔ Revenue
- UnitPrice ↔ Revenue

### ⚠️ Important Statistical Note

Revenue is mathematically derived from:

```text
Revenue = Quantity × UnitPrice
```

Therefore, correlations involving Revenue are partly induced by this mathematical relationship.

Correlation was interpreted as **association**, not causation.

---

# 📅 Time-Based Analysis

Time-based analysis was performed using:

- Monthly revenue trends
- Day-of-week patterns
- Transaction timing

Regular-sales analysis used positive-quantity transactions to avoid directly mixing normal sales activity with negative transaction effects.

The findings describe the historical observation period represented by the dataset and should not automatically be generalized to future periods.

---

# 📐 Hypothesis Testing

## Mann–Whitney U Test

A two-sided **Mann–Whitney U test** was performed to compare order-value distributions between:

### 🇬🇧 United Kingdom

and

### 🇩🇪 Germany

| Statistic | Result |
|---|---:|
| United Kingdom orders | **18,019** |
| Germany orders | **457** |
| UK median order value | **299.95** |
| Germany median order value | **354.85** |
| U Statistic | **3,489,572.50** |
| p-value | **< 0.000001** |
| Rank-biserial effect size | **0.1525** |

### 🧠 Interpretation

The statistical test provides evidence of a difference between the observed order-value distributions.

However:

> **Statistical significance ≠ practical significance**

and:

> **Association ≠ causation**

The result describes the observed dataset and does not establish that country itself causes differences in order value.

---

# 🧠 Data-Handling Philosophy

Throughout the analysis, major data decisions followed this framework:

```text
Observed Data
      ↓
Why is this happening?
      ↓
What are the alternatives?
      ↓
What is the analytical impact?
      ↓
What does it mean for the business?
```

This approach helps preserve potentially meaningful information while making assumptions and limitations explicit.

---

# ⚠️ Assumptions & Limitations

- Negative quantities may represent returns, cancellations, credits, or reversals.
- Every negative transaction cannot be definitively classified from the available fields.
- Statistical outliers are not necessarily data errors.
- `CustomerID` values were not artificially inferred.
- Revenue does not represent profit.
- Product costs and operating expenses are unavailable.
- Correlation does not imply causation.
- Revenue is mathematically derived from `Quantity` and `UnitPrice`.
- Customer analysis represents only records with available `CustomerID`.
- The hypothesis test describes the observed dataset and does not establish causality.
- Findings describe the available historical dataset and should not automatically be generalized to other businesses or future periods.

---

# 💡 Key Findings

### 01 — Dataset Quality

The final EDA dataset contains:

**534,129 records**

with:

**0 duplicate rows**

---

### 02 — Negative Transactions

**9,251 transactions (1.73%)**

contain negative quantities.

Their combined quantity is:

**-275,560**

and their revenue impact is:

**-893,979.73**

---

### 03 — Revenue

Regular positive-quantity revenue:

**10,642,110.80**

Net recorded revenue:

**9,748,131.07**

---

### 04 — Customer Analytics

Identified customers:

**4,338**

Identified-customer orders:

**18,532**

Overall invoice-level AOV:

**479.56**

---

### 05 — Product Analysis

Highest-revenue dataset line item:

**DOTCOM POSTAGE**

Revenue:

**206,248.77**

---

### 06 — Country Analysis

Highest recorded regular-sales revenue:

**United Kingdom**

Revenue:

**9,001,744.09**

---

### 07 — Statistical Analysis

Mann–Whitney U:

**3,489,572.50**

p-value:

**< 0.000001**

Rank-biserial effect size:

**0.1525**

---

# 📄 Project Deliverables

## 🧹 Week 1

📓 `notebooks/Week_1_Data_Cleaning.ipynb`

📄 `report/Week_1_Data_Cleaning_Report.pdf`

---

## 📊 Week 2

📓 `notebooks/Week_2_EDA.ipynb`

📄 `report/Week_2_EDA_Report.pdf`

---

# 🚀 Skills Developed

```text
Python
│
├── Data Cleaning
├── Data Validation
├── Missing Value Analysis
├── Duplicate Detection
├── Outlier Investigation
│
├── Exploratory Data Analysis
├── Descriptive Statistics
├── Data Visualization
├── Correlation Analysis
├── Time-Based Analysis
│
├── Customer Analytics
├── Product Analytics
├── Geographic Analysis
├── Revenue Analysis
├── AOV Analysis
│
├── Hypothesis Testing
├── Effect Size
├── Statistical Interpretation
│
└── Business Insight Generation
```

---

# 🔁 Reproducibility

The project uses:

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
SciPy
Jupyter Notebook
VS Code
Git
GitHub
```

Visualization sampling uses:

```python
random_state = 42
```

to improve reproducibility.

---

# 🗺️ Upcoming Internship Roadmap

| Week | Planned Focus | Status |
|---|---|---|
| 🧹 Week 1 | Data Cleaning & Preprocessing | ✅ |
| 📊 Week 2 | Exploratory Data Analysis | ✅ |
| ⚙️ Week 3 | Advanced Analysis / Feature Engineering | 🔜 |
| 🤖 Week 4 | Machine Learning | 🔜 |
| 📈 Week 5 | Model Evaluation & Improvement | 🔜 |
| 🏆 Week 6 | Final Data Science Project | 🔜 |

---

# 👨‍💻 About Me

<div align="center">

## Anand Yadav

### MCA Student • Aspiring Data Scientist • Data Analytics Enthusiast

</div>

I am currently building practical skills in:

- 📊 Data Science
- 🤖 Machine Learning
- 📈 Data Analytics
- 🧠 Artificial Intelligence
- 📉 Business Intelligence
- 🐍 Python
- 💻 Software Development

My goal is to continuously improve my ability to transform raw data into meaningful insights and practical solutions.

---

# 🏆 Internship Mission

This repository is more than a collection of weekly assignments.

It represents a practical journey of:

<div align="center">

### **RAW DATA**
↓  
### **RELIABLE DATA**
↓  
### **EXPLORATION**
↓  
### **STATISTICAL EVIDENCE**
↓  
### **BUSINESS INSIGHTS**
↓  
### **DATA-DRIVEN DECISIONS**

</div>

---

# ⭐ Final Goal

> **Learn → Build → Analyze → Interpret → Improve → Repeat**

---

<div align="center">

### 🚀 Junior Data Science Internship — 2026

**Building Data Science Skills One Week at a Time.**

</div>