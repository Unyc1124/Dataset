# Python Code for Data Preprocessing #

import pandas as pd

# Read the raw text file
with open("CSI_gyro_10_5.txt", "r") as file:
    lines = file.readlines()

# Filter and clean only data lines (ignore headers/comments)
data = []
for line in lines:
    if line.strip() and not line.startswith("#") and not line.startswith("@"):
        # Split and remove any commas attached to numbers
        cleaned = [value.strip().rstrip(',') for value in line.strip().split()]
        data.append(cleaned)

# Create DataFrame with headers
df = pd.DataFrame(data, columns=["Timestamp (ns)", "X (rad/s)", "Y (rad/s)", "Z (rad/s)"])

# Convert columns to appropriate data types
df["Timestamp (ns)"] = df["Timestamp (ns)"].astype("int64")
df["X (rad/s)"] = df["X (rad/s)"].astype("float32")
df["Y (rad/s)"] = df["Y (rad/s)"].astype("float32")
df["Z (rad/s)"] = df["Z (rad/s)"].astype("float32")

# Save to CSV
df.to_csv("CSI_gyro_10_5_converted.csv", index=False)
print("✅ CSV file saved as CSI_gyro_10_5_converted.csv")
