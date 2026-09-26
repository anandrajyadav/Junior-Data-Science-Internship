import pandas as pd


# ==============================
# File Paths
# ==============================

INPUT_FILE = "../data/raw/Online Retail.xlsx"
OUTPUT_FILE = "../data/cleaned/Online_Retail_Cleaned.csv"


# ==============================
# Load Dataset
# ==============================

df = pd.read_excel(INPUT_FILE)

print("Original dataset shape:", df.shape)


# ==============================
# Remove Exact Duplicates
# ==============================

df = df.drop_duplicates().copy()


# ==============================
# Data Type Conversion
# ==============================

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"],
    errors="coerce"
)


# ==============================
# Handle Missing Description
# ==============================

df["Description"] = df["Description"].fillna(
    "Unknown Product"
)


# ==============================
# Remove Invalid Unit Prices
# ==============================

df = df[df["UnitPrice"] > 0].copy()


# ==============================
# Save Cleaned Dataset
# ==============================

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==============================
# Final Validation
# ==============================

print("Cleaned dataset shape:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print(
    "Invalid UnitPrice:",
    (df["UnitPrice"] <= 0).sum()
)
print("Missing values:")
print(df.isnull().sum())

print("\nCleaned dataset saved successfully.")
print("Output:", OUTPUT_FILE)