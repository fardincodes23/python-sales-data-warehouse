from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_sales_data(num_records=100):
    data = []
    products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
    
    for _ in range(num_records):
        data.append({
            'order_id': fake.uuid4(),
            'customer_name': fake.name(),
            'product': random.choice(products),
            'quantity': random.randint(1, 10),
            'price': round(random.uniform(50, 1500), 2),
            'order_date': fake.date_between(start_date='-1y', end_date='today'),
            'country': fake.country()
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sales_data()
    df.to_csv('raw_sales_data.csv', index=False)
    print(f"Generated {len(df)} records")
    print(df.head())