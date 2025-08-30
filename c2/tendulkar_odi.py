import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('tendulkar_ODI.csv')

# Filter out non-numeric values (DNB, TDNB)
df = df[pd.to_numeric(df['Runs'], errors='coerce').notna()]
df['Runs'] = pd.to_numeric(df['Runs'])

# Create bins for runs scored
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 200]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', 
          '70-79', '80-89', '90-99', '100-109', '110-119', '120+']

# Group the data into bins
runs_binned = pd.cut(df['Runs'], bins=bins, labels=labels, right=False)
run_counts = runs_binned.value_counts().sort_index()

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(run_counts.index, run_counts.values)
plt.xlabel('Runs Scored')
plt.ylabel('Frequency (Number of Innings)')
plt.title('Distribution of Sachin Tendulkar\'s ODI Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Find the bucket with the highest frequency
most_frequent_bucket = run_counts.idxmax()
most_frequent_count = run_counts.max()

# Filter out non-numeric values in the '4s' column
df = df[pd.to_numeric(df['4s'], errors='coerce').notna()]
df['4s'] = pd.to_numeric(df['4s'])

# Create a histogram of the number of 4s
plt.figure(figsize=(12, 6))
plt.hist(df['4s'], bins=range(0, df['4s'].max()+2), align='left', rwidth=0.8)
plt.xlabel('Number of Fours')
plt.ylabel('Frequency (Number of Innings)')
plt.title('Distribution of Fours Hit by Sachin Tendulkar in ODIs')
plt.xticks(range(0, df['4s'].max()+1))
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

# Find the most common value (mode) of 4s
most_common_fours = df['4s'].mode()[0]
most_common_count = df['4s'].value_counts()[most_common_fours]

# Annotate the most common value
plt.axvline(x=most_common_fours, color='r', linestyle='--')
plt.text(most_common_fours + 0.5, plt.ylim()[1]*0.9, 
         f'Most common: {most_common_fours} fours\n({most_common_count} innings)', 
         color='r')

plt.show()

print(f"The most common number of fours hit by Tendulkar in an ODI innings is {most_common_fours}")