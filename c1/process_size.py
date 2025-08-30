import pandas as pd

def process_size_column(csv_path):
    df = pd.read_csv(csv_path)
    
    def map_size(val):
        if pd.isnull(val):
            return val
        val_str = str(val).strip().lower()
        if val_str in ['s', 'small']:
            return 'Small'
        elif val_str == 'm':
            return 'Medium'
        elif val_str == 'l':
            return 'Large'
        elif val_str == 'xl':
            return 'Extra large'
        elif val_str == 'free':
            return 'Free'
        else:
            return val
    
    df['Size'] = df['Size'].apply(map_size)
    
    # Calculate percentages
    size_counts = df['Size'].value_counts(normalize=True) * 100
    lowest = size_counts.min()
    highest = size_counts.max()
    small_pct = size_counts.get('Small', 0)
    
    print(f"Lowest percentage: {lowest:.2f}%")
    print(f"Highest percentage: {highest:.2f}%")
    print(f"Percentage of Small: {small_pct:.2f}%")
    
    return df, lowest, highest, small_pct

if __name__ == "__main__":
    csv_path = 'Attribute+DataSet (2).csv'
    process_size_column(csv_path)
