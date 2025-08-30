import pandas as pd

# Read the CSV file
df = pd.read_csv('EDA_Gold_Silver_prices.csv')

# Calculate the correlation between Gold and Silver prices
correlation = df['GoldPrice'].corr(df['SilverPrice'])

# Round to two decimal places
correlation_rounded = round(correlation, 2)

print(correlation_rounded)

df_2008 = df[df['Month'].str.contains('-08$')]

# Calculate the correlation between Gold and Silver prices for 2008
correlation_2008 = df_2008['GoldPrice'].corr(df_2008['SilverPrice'])

# Round to two decimal places
correlation_rounded = round(correlation_2008, 2)

print(correlation_rounded)