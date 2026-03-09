import pandas as pd

print("Loading dataset...")

df = pd.read_csv("complaints.csv")

print("Dataset loaded.")

# Keep only the columns needed for analysis
columns = [
    "Date received",
    "Product",
    "Sub-product",
    "Issue",
    "Sub-issue",
    "Company",
    "State",
    "Submitted via",
    "Company response to consumer",
    "Timely response?",
    "Complaint ID"
]

clean_df = df[columns].copy()

# Save smaller clean dataset
clean_df.to_csv("financial_complaints_clean.csv", index=False)

print("Clean dataset created.")
print("Rows:", len(clean_df))
print("Columns:", list(clean_df.columns))
