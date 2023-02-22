# review_checker
## Описание
Небольшой скрипт для оценки отзыва по 10-бальной шкале. Необходимо поместить отзывы в csv файл review(пример его заполнения уже находится в репозитории) и запустить скрип main.py. Проанализированные отзывы сохраняются в файл reviews_analyzed.csv

## Установка
```
git clone https://github.com/danyadanyaa/review_checker
```

#### Создайте файл .env в корнейвой директории и добавьте переменные окружения:
```
api_key='Ваш api ключ OpenAI можно получить здесь https://platform.openai.com/'
```
#### Установите необходимые модули:
```
pip install -r requirements.exe
```
#### Запустите скрипт:
```
python main.py
```
