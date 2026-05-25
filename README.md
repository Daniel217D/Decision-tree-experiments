# Проект анализа данных (шаблон)

Шаблон для анализа данных

## Структура

- **main.ipynb** — один ноутбук: настройка, загрузка данных, предобработка, профили, EDA, выводы.
- **requirements.txt** — зависимости Python.
- **.env.example** — скопируйте в `.env` и задайте переменные (например, строку подключения при загрузке из БД).

## Быстрый старт

1. Клонируйте проект.
2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # или .venv\Scripts\activate в Windows
   pip install -r requirements.txt
   ```
3. Скопируйте `.env.example` в `.env` и задайте нужные переменные.
4. Откройте `main.ipynb` и приступайте

## Стек

- Python, pandas, numpy  
- python-dotenv для `.env`  
- phik, matplotlib, seaborn
- Jupyter для ноутбука
