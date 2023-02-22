import os
import pandas as pd
import openai
from dotenv import load_dotenv
# загрузка переменных окружения
load_dotenv()

# установка ключа API OpenAI
openai.api_key = os.getenv('api_key')


# функция для получения оценки интонации текста
def get_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Rate the following review on a scale of 1 to 10 based on the tone and sentiment of the text, print just a rate:\n{text}\nRate:"),
        max_tokens=1,
    )
    return int(response.choices[0].text)


# чтение файла с данными
input_file = "reviews.csv"
df = pd.read_csv(input_file)

# применение функции к каждому отзыву в таблице и сохранение оценок в новую колонку
df["rate"] = df["review text"].apply(get_sentiment)

# сортировка таблицы по убыванию оценки
df = df.sort_values("rate", ascending=False)

# запись таблицы в новый файл
output_file = f"{os.path.splitext(input_file)[0]}_analyzed.csv"
df.to_csv(output_file, index=False)

print(f"Результаты анализа сохранены в файл: {output_file}")
