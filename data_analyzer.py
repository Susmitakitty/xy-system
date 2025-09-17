import pandas as pd

# Read sensor data
try:
    df = pd.read_csv("sensor_data.csv")
except FileNotFoundError:
    print("Error: sensor_data.csv not found. Run data_collector.py first.")
    exit()

# Basic statistics
summary = {
    "Total Records": len(df),
    "Average Temperature": df["temperature"].mean(),
    "Max Temperature": df["temperature"].max(),
    "Min Temperature": df["temperature"].min(),
    "Average Vibration": df["vibration"].mean(),
    "Max Vibration": df["vibration"].max(),
    "Min Vibration": df["vibration"].min(),
}

# Save to file
with open("analysis_summary.txt", "w") as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

print("✅ Analysis complete → results saved in analysis_summary.txt")
