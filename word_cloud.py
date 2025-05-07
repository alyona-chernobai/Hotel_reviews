import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk
import os

# Скачиваем стоп-слова, если ещё не скачаны
nltk.download('stopwords')

# Загружаем данные
df = pd.read_csv('tripadvisor_hotel_reviews.csv')

# Стоп-слова
stop_words = set(stopwords.words('english'))

# Категоризация отзывов
def categorize_reviews(df):
    df = df.copy()
    df['Review_Category'] = df['Rating'].apply(
        lambda x: 'Positive' if x >= 4 else ('Negative' if x <= 2 else 'Neutral')
    )
    return df[df['Review_Category'] != 'Neutral']

# Функция генерации и сохранения облаков слов
def create_wordclouds(df, output_dir="Hotel_reviews/output", general_output=True):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    categories = {
        "Positive": {"colormap": "Greens", "bg": "white"},
        "Negative": {"colormap": "Reds", "bg": "black"}
    }

    for category, params in categories.items():
        text = ' '.join(df[df["Review_Category"] == category]["Review"].dropna())
        wc = WordCloud(
            width=1200, height=600,
            background_color=params["bg"],
            stopwords=stop_words,
            colormap=params["colormap"],
            max_words=200
        ).generate(text)
        filename = f'wordcloud_{category.lower()}.png'
        wc.to_file(os.path.join(output_dir, filename))

    if general_output:
        text_all = ' '.join(df["Review"].dropna())
        wc_all = WordCloud(
            width=1200, height=600,
            background_color='gray',
            stopwords=stop_words,
            max_words=200
        ).generate(text_all)
        wc_all.to_file(os.path.join(output_dir, 'wordcloud_all.png'))

    print("✅ WordCloud-файлы сохранены в:", output_dir)

# Обработка
df = categorize_reviews(df)
create_wordclouds(df)
