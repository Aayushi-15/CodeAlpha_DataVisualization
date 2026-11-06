import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("books_data.csv", encoding="utf-8-sig")

# Clean price data
df["Price"] = (
    df["Price"].astype(str)
    .str.replace(r"[^0-9.]", "", regex=True)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Price"])

# Create charts folder
os.makedirs("charts", exist_ok=True)

# 1. Bar Chart - Top 10 expensive books
top_books = df.nlargest(10, "Price")

plt.figure(figsize=(12, 6))
plt.bar(top_books["Title"], top_books["Price"])
plt.title("Top 10 Expensive Books")
plt.xlabel("Book Titles")
plt.ylabel("Price")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.show()

# 2. Histogram - Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("charts/histogram.png")
plt.show()

# 3. Pie Chart - Availability
availability = df["Availability"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    availability,
    labels=availability.index,
    autopct="%1.1f%%"
)
plt.title("Book Availability")
plt.savefig("charts/pie_chart.png")
plt.show()

print("Data Visualization Completed!")
print("Total books:", len(df))
print("Average price:", round(df["Price"].mean(), 2))
print("Charts saved successfully in charts folder.")