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