import pandas as pd

# Read the data
df = pd.read_csv('odi-batting.csv')

# Find centuries by Indian players
india_centuries = df[(df['Country'] == 'India') & (df['Runs'] >= 100)].copy()

# Extract year from the date (assuming date format is DD-MM-YYYY)
india_centuries['Year'] = india_centuries['MatchDate'].str.split('-').str[-1]

# Count centuries per year
centuries_by_year = india_centuries.groupby('Year').size().reset_index(name='Number of Centuries')

# Find the year with maximum centuries
max_centuries_year = centuries_by_year.loc[centuries_by_year['Number of Centuries'].idxmax()]

print(f"\nYear with maximum number of centuries by Indian players: {max_centuries_year['Year']}")
print(f"Number of centuries scored in that year: {max_centuries_year['Number of Centuries']}")

# Display the top 5 years with most centuries
print("\nTop 5 years with most centuries by Indian players:")
top_years = centuries_by_year.sort_values('Number of Centuries', ascending=False).head(5)
print(top_years)

# Show some details about centuries in the max year
print(f"\nDetails of centuries scored by Indian players in {max_centuries_year['Year']}:")
max_year_centuries = india_centuries[india_centuries['Year'] == max_centuries_year['Year']]
player_summary = max_year_centuries.groupby('Player')['Runs'].agg(['count', 'mean', 'min', 'max']).reset_index()
player_summary.columns = ['Player', 'Centuries', 'Average Score', 'Lowest Score', 'Highest Score']
player_summary = player_summary.sort_values('Centuries', ascending=False)
print(player_summary)
