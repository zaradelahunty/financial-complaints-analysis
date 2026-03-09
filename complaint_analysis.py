import pandas as pd
import matplotlib.pyplot as plt

print("Loading clean dataset...")

df = pd.read_csv("financial_complaints_clean.csv")

print("Dataset loaded.")
print("Rows:", len(df))


# -----------------------------
# Complaints by Product
# -----------------------------
product_counts = df["Product"].value_counts().head(10)

plt.figure(figsize=(10,6))
product_counts.plot(kind="bar")
plt.title("Top Financial Products by Complaint Volume")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("complaints_by_product.png")


# -----------------------------
# Complaints by State
# -----------------------------
state_counts = df["State"].value_counts().head(10)

plt.figure(figsize=(10,6))
state_counts.plot(kind="bar")
plt.title("Top States by Complaint Volume")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("complaints_by_state.png")


# -----------------------------
# Complaints Over Time
# -----------------------------
df["Date received"] = pd.to_datetime(df["Date received"])
year_counts = df["Date received"].dt.year.value_counts().sort_index()

plt.figure(figsize=(10,6))
year_counts.plot(kind="line")
plt.title("Consumer Complaints Over Time")
plt.ylabel("Number of Complaints")
plt.xlabel("Year")
plt.tight_layout()
plt.savefig("complaints_over_time.png")

print("Charts created successfully.")