# Junior Data Science Internship — Week 1

## Data Gathering, Cleaning and Preprocessing

This project is part of my Junior Data Science Internship.

The objective of Week 1 was to collect a publicly available retail dataset, explore its structure, identify data-quality issues, clean and preprocess the data, and prepare a final dataset suitable for further analysis.

## Dataset

The project uses the Online Retail dataset containing transaction-level retail information.

### Main Columns

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

## Data Cleaning Performed

The following preprocessing steps were performed:

1. Initial dataset exploration
2. Missing-value analysis
3. Duplicate detection and removal
4. Data type conversion
5. Missing product descriptions handled using `Unknown Product`
6. Invalid `UnitPrice` values identified and removed
7. Negative quantities retained because they may represent returns or cancellations
8. Statistical outliers investigated using the IQR method
9. Final data-quality validation
10. Cleaned dataset exported as CSV

## Outlier Treatment

Statistical outliers were identified using the Interquartile Range (IQR) method.

Outliers were not automatically removed because unusual retail transactions may represent legitimate bulk purchases or high-value products.

## Missing Values

`CustomerID` values that were unavailable were retained as missing because customer identifiers cannot be reliably inferred from the available data.

Missing product descriptions were represented as `Unknown Product`.

## Project Structure

```text
Junior-Data-Science-Internship/
│
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx
│   │
│   └── cleaned/
│       └── Online_Retail_Cleaned.csv
│
├── notebooks/
│   └── Week_1_Data_Cleaning.ipynb
│
├── report/
│
├── src/
│   └── data_cleaning.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

# 📊 Week 2 — Exploratory Data Analysis (EDA)

### Objective

The objective of Week 2 was to perform comprehensive Exploratory Data Analysis (EDA) on the cleaned Online Retail dataset prepared during Week 1.

The analysis focused on understanding distributions, relationships, trends, customer behaviour, product performance, country-level sales, negative transactions, outliers, and statistical differences between groups.

### Dataset

- **Dataset:** Online Retail
- **Source:** Week 1 cleaned dataset
- **Rows analyzed:** 534,129
- **Duplicate rows:** 0
- **Original numerical variables:** Quantity, UnitPrice
- **Derived variable:** Revenue = Quantity × UnitPrice

### Key Analysis Performed

- Descriptive statistics
- Mean, median, variance, standard deviation and skewness
- Revenue calculation
- Negative quantity analysis
- Country-level return/reversal analysis
- Product-level negative quantity analysis
- IQR-based outlier detection
- Box plot analysis
- Histogram and distribution analysis
- Correlation analysis
- Scatter plot analysis
- Monthly revenue trend analysis
- Day-of-week analysis
- Product-level revenue analysis
- Country-level revenue analysis
- Customer-level analysis
- Average Order Value (AOV)
- Negative transaction revenue impact
- Mann–Whitney U hypothesis testing
- Effect-size analysis
- Assumptions and limitations analysis

### Important Findings

- The cleaned dataset contains **534,129 records** with **0 duplicate rows**.
- **9,251 transactions (1.73%)** contain negative quantities.
- Negative quantities represent a total quantity of **-275,560**.
- Negative transactions reduce recorded revenue by **893,979.73**.
- Regular positive-quantity sales revenue is **10,642,110.80**.
- Net recorded revenue after negative transaction effects is **9,748,131.07**.
- Customer-level analysis identified **4,338 customers** with available CustomerID.
- Identified-customer orders: **18,532**.
- Overall invoice-level AOV: **479.56**.
- The highest-revenue dataset line item was **DOTCOM POSTAGE**, with recorded revenue of **206,248.77**.
- The United Kingdom recorded the highest regular-sales revenue in this analysis at **9,001,744.09**.

### Hypothesis Testing

A two-sided **Mann–Whitney U test** was performed to compare order-value distributions between the two countries with the highest regular-sale transaction counts.

- Group 1: United Kingdom
- Group 2: Germany
- United Kingdom orders: 18,019
- Germany orders: 457
- United Kingdom median order value: 299.95
- Germany median order value: 354.85
- U Statistic: 3,489,572.50
- p-value: < 0.000001
- Rank-biserial effect size: 0.1525

The statistical result indicates evidence of a difference between the observed order-value distributions. Statistical significance was interpreted separately from practical significance and was not treated as evidence of causation.

### Data-Handling Decisions

Negative quantities were retained because they may represent returns, cancellations, credit transactions, or other reversals. They were analyzed separately from regular positive-quantity sales.

Outliers were identified using the IQR method but were not automatically removed because extreme retail transactions can represent legitimate business activity.

Missing CustomerID values were not artificially inferred because reliable customer identification was not possible from the available data.

### Limitations

- Negative quantities cannot be definitively classified without additional transaction-status information.
- Statistical outliers are not necessarily data errors.
- Revenue does not represent profit because cost and operating-expense information is unavailable.
- Correlation does not imply causation.
- Revenue is mathematically derived from Quantity and UnitPrice.
- Customer analysis represents only transactions with an available CustomerID.
- Findings describe the available historical dataset and should not automatically be generalized to other businesses or future periods.

### Week 2 Deliverables

- `notebooks/Week_2_EDA.ipynb`
- `report/Week_2_EDA_Report.pdf`

---