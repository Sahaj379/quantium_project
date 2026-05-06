import pandas as pd
import glob

# Load all CSV files from current folder
files = glob.glob("*.csv")

# Store all dataframes
df_list = []

# Read each CSV file
for file in files:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

# Combine all CSV files into one dataframe
df = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsel rows
pink_df = df[df["product"] == "pink morsel"]

# Remove $ symbol from price and convert to float
pink_df["price"] = pink_df["price"].replace("[$]", "", regex=True).astype(float)

# Convert date column to datetime format
pink_df["date"] = pd.to_datetime(pink_df["date"])

# Create sales column
pink_df["sales"] = pink_df["price"] * pink_df["quantity"]

# Create final output dataframe
output_df = pink_df[["sales", "date", "region"]]

# Show final output
print(output_df.head())

# Save final cleaned data to CSV
output_df.to_csv("formatted_output.csv", index=False)

print("Formatted output file created successfully.")