import pandas as pd
import glob

files = glob.glob("*.csv")

df_list = []

for file in files:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

print(df.columns)

print(df.info())

print(df.head())


#pink_df = df[df["product"] == "Pink Morsel"]

#print(df.columns)

pink_df = df[df["product"] == "pink morsel"]

print(pink_df.head())

# Remove $ symbol and convert price to float
pink_df["price"] = pink_df["price"].replace("[$]", "", regex=True).astype(float)

# Check result
print(pink_df.head())
print(pink_df.info())

# Convert date column to datetime format
pink_df["date"] = pd.to_datetime(pink_df["date"])

# Check updated data types
print(pink_df.info())


# Create sales column
pink_df["sales"] = pink_df["price"] * pink_df["quantity"]

# Check result
print(pink_df.head())





# Split data before and after price increase date
before = pink_df[pink_df["date"] < "2021-01-15"]

after = pink_df[pink_df["date"] >= "2021-01-15"]

# Calculate total sales
before_sales = before["sales"].sum()

after_sales = after["sales"].sum()

# Print results
print("Sales Before Jan 15, 2021:", before_sales)

print("Sales After Jan 15, 2021:", after_sales)




# Business conclusion
if after_sales > before_sales:
    print("Sales increased after the price increase.")
else:
    print("Sales decreased after the price increase.")