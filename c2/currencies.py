import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('currencies.csv')

# Set the date column as index
df['Currency'] = pd.to_datetime(df['Currency'])
df = df.set_index('Currency')

# Convert string values with commas to float
for col in df.columns:
    df[col] = df[col].replace('NA', np.nan)
    df[col] = df[col].apply(lambda x: float(str(x).replace(',', '')) if pd.notnull(x) else x)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Find currencies most correlated with Indian Rupee
indian_rupee_correlations = correlation_matrix['Indian Rupee'].sort_values(ascending=False)
print("Currencies most correlated with Indian Rupee:")
print(indian_rupee_correlations)

# Extract the subset of major currencies
major_currencies = ['Chinese Yuan', 'Euro', 'Japanese Yen', 'U.K. Pound Sterling', 
                    'U.S. Dollar', 'Australian Dollar', 'Indian Rupee']

# Get correlation matrix for these currencies
major_corr = correlation_matrix.loc[major_currencies, major_currencies]

# Display the correlation matrix with formatting
plt.figure(figsize=(10, 8))
sns.heatmap(major_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix of Major Currencies')
plt.tight_layout()
plt.show()

# Find most negatively correlated pair
min_corr = 1
min_pair = None

for i in range(len(major_currencies)):
    for j in range(i+1, len(major_currencies)):
        curr_i = major_currencies[i]
        curr_j = major_currencies[j]
        corr = major_corr.loc[curr_i, curr_j]
        if corr < min_corr:
            min_corr = corr
            min_pair = (curr_i, curr_j)

print(f"Most negatively correlated pair: {min_pair[0]} and {min_pair[1]} (correlation: {min_corr:.3f})")