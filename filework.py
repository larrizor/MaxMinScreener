import json, os, client
from loguru import logger

def write_list_of_tickers(tickers: list):
    # Назва файлу
    file_name = "binance_tickers.json"

    # Запис в файл
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            # indent=4 робить файл читабельним для людини (додає відступи)
            # ensure_ascii=False дозволяє коректно зберігати кирилицю
            json.dump(tickers, file, indent=4, ensure_ascii=False)

        print(f"Список успішно записано у файл {file_name}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def read_list_from_json(file_name):
    # Перевіряємо, чи існує файл перед відкриттям
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не знайдено!")
        return []  # Повертаємо порожній список, якщо файлу нема

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Помилка при читанні: {e}")
        return []


def save_levels_to_json(structured_data, file_name):
    # Перетворюємо вхідний список у список словників (пари тікер-рівень)
    # Приклад припускає, що вхідні дані - це кортежі або вкладені списки
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не знайдено!")
        return []  # Повертаємо порожній список, якщо файлу нема
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=4, ensure_ascii=False)
        print(f"Дані успішно збережено у {file_name}")
    except Exception as e:
        print(f"Помилка запису: {e}")


def find_ticker_level(file_name, search_ticker):
    # 1. Проверяем, существует ли файл
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        return None

    try:
        # 2. Читаем данные из файла
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        # 3. Ищем нужный тикер в списке словарей
        for item in data:
            # Сравниваем тикеры (приводим к верхнему регистру для надежности)
            if item.get("ticker").upper() == search_ticker.upper():
                return item.get("level")

        print(f"Тикер {search_ticker} не найден в файле.")
        return None

    except Exception as e:
        print(f"Ошибка при поиске: {e}")
        return None