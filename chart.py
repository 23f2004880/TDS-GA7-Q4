# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic seasonal revenue data
np.random.seed(42)
months = pd.date_range(start="2023-01", periods=12, freq="M")
departments = ["Electronics", "Clothing", "Groceries"]

data = []
for dept in departments:
    base = np.linspace(20000, 35000, 12)  # increasing trend
    seasonal = 5000 * np.sin(np.linspace(0, 2*np.pi, 12))  # seasonal variation
    noise = np.random.normal(0, 2000, 12)  # randomness
    revenue = base + seasonal + noise + (departments.index(dept) * 3000)
    for m, r in zip(months, revenue):
        data.append([m, dept, r])

df = pd.DataFrame(data, columns=["Month", "Department", "Revenue"])

# Create figure with exact dimensions for 512x512 px
# figsize (inches) * dpi = pixels → 5.12 * 100 = 512
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Lineplot
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Department",
    marker="o",
    palette="Set2"
)

# Titles and labels
plt.title("Monthly Revenue Trends by Department (2023)", fontsize=14, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Save without bbox_inches="tight" to preserve exact dimensions
plt.savefig("chart.png", dpi=100)
plt.close()
