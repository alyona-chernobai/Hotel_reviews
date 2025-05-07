import pandas as pd

def load_and_prepare_data(csv_path):
    df = pd.read_csv(csv_path)

    # Категория настроения
    df["Review_Category"] = df["Rating"].apply(
        lambda x: "Positive" if x >= 4 else ("Negative" if x <= 2 else "Neutral")
    )

    # Длина отзыва
    df["Review_Length"] = df["Review"].astype(str).str.len()

    return df

# Загружаем и обрабатываем данные
df = load_and_prepare_data('tripadvisor_hotel_reviews.csv')

# Сохраняем обработанный CSV
df.to_csv('tripadvisor_reviews_ready.csv', index=False, encoding='utf-8')
print("✅ Готовый файл сохранен как 'tripadvisor_reviews_ready.csv'!")
