import pandas as pd
import random

def add_random_city(df):
    cities = [
        'London', 'Paris', 'New York', 'Tokyo', 'Berlin',
        'Rome', 'Amsterdam', 'Madrid', 'Toronto', 'Dubai',
        'Bangkok', 'Vienna', 'Chicago', 'Sydney', 'Barcelona'
    ]
    df['City'] = [random.choice(cities) for _ in range(len(df))]
    df.to_csv('tripadvisor_reviews_with_city.csv', index=False)
    print("✅ Файл с городами сохранён как 'tripadvisor_reviews_with_city.csv'!")
    return df

# Основной блок запуска
if __name__ == "__main__":
    df = pd.read_csv('tripadvisor_reviews_ready.csv')
    df = add_random_city(df)
