import pandas as pd

def transform_data(filepath='raw_sales_data.csv'):
    # Load raw data
    df = pd.read_csv(filepath)
    print(f"Raw records: {len(df)}")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Add total_sale column
    df['total_sale'] = df['quantity'] * df['price']

    # Standardize country to uppercase
    df['country'] = df['country'].str.upper()

    # Convert order_date to datetime
    df['order_date'] = pd.to_datetime(df['order_date'])

    print(f"Clean records: {len(df)}")
    print(df.head())
    
    return df

if __name__ == "__main__":
    transform_data()