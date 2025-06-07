import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("part_deviation_data.csv")

df["deviation"] = df["actual"] - df["expected"]
df["abs_deviation"] = df["deviation"].abs()

mean_deviation = df["deviation"].mean()
std_deviation = df["deviation"].std()
mse = np.mean(df["deviation"] ** 2)

print(df)
print("\nError Metrics:")
print(f"Mean Deviation: {mean_deviation:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")

df.to_csv("part_deviation_results.csv", index=False)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(df["part"], df["deviation"], color="orange")
plt.axhline(0, color="black", linestyle="--")
plt.title("Deviation (Actual - Expected)")
plt.xlabel("Car Part")
plt.ylabel("Deviation")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.subplot(1, 2, 2)
plt.bar(df["part"], df["abs_deviation"], color="skyblue")
plt.title("Absolute Deviation")
plt.xlabel("Car Part")
plt.ylabel("Absolute Deviation")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()