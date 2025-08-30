
# Dress Sales Season Analysis Script
import pandas as pd

# Load the data
df = pd.read_csv('Dress+Sales (1).csv')

# Melt the dataframe to long format
df_long = df.melt(id_vars='Dress_ID', var_name='Date', value_name='Sales')

# Convert 'Date' to datetime, coerce errors for non-date columns
df_long['Date'] = pd.to_datetime(df_long['Date'], dayfirst=True, errors='coerce')

# Drop rows where 'Date' is NaT
df_long = df_long.dropna(subset=['Date'])

# Extract month
df_long['Month'] = df_long['Date'].dt.month

# Map months to seasons
def get_season(month):
    if month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    elif month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'

df_long['Season'] = df_long['Month'].apply(get_season)

# Convert Sales to numeric
df_long['Sales'] = pd.to_numeric(df_long['Sales'], errors='coerce')

# Group by season and sum sales
season_sales = df_long.groupby('Season')['Sales'].sum()

# Find the season with the lowest sales
lowest_season = season_sales.idxmin()
lowest_value = season_sales.min()

print('Total sales by season:')
print(season_sales)
print(f"\nThe season with the lowest sales is {lowest_season} with a value of {lowest_value}.")