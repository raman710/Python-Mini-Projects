import pandas as pd

df = pd.read_csv("sales.csv")

print("SALES DATA ANALYZER")
print("-" * 40)

print(df.head())

# Total Sales
df["Total"] = df["Price"] * df["Quantity"]

print("\nTotal Revenue:", df["Total"].sum())

print("\nBest Selling Category:")
print(df.groupby("Category")["Quantity"].sum())

print("\nMost Expensive Product:")
print(df.loc[df["Price"].idxmax()])

df.to_csv("sales_analysis.csv", index=False)

print("\nAnalysis Saved Successfully!")