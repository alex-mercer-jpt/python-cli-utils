"""
Учебный CLI-проект: утилиты для работы с числами и текстом.
Запуск: python main.py
"""

# Импорт конкретных функций
from sandbox.hello_name import handle_hello
from sandbox.location_time import handle_location_time
from sandbox.check_range import handle_check_range
from sandbox.letter_check import handle_letter_check
from sandbox.number_formatting import handle_number_formatting
from sandbox.clean_text import handle_clean_text
from sandbox.average_word_length import handle_average_word_length
from sandbox.max_values import handle_max_values
from sandbox.unique_chars import handle_unique_chars
from sandbox.word_frequency import handle_word_frequency
# Импорт модуля целиком
from sandbox import word_filter
from sandbox import average_calc
from sandbox import text_processor
from sandbox import map_lambda_range
from sandbox import fibonacci
from sandbox import my_map
from sandbox import my_filter
from sandbox import decorator_cache
from sandbox import decorator_repeat
from sandbox import global_var
from sandbox import nonlocal_var

def main() -> None:
    menu = {
        # Импорт конкретных функций
        "1": ("Приветствие по имени", handle_hello),
        "2": ("Текущая локация и время", handle_location_time),
        "3": ("Проверка чисел в диапазоне", handle_check_range),
        "4": ("Проверка букв в строке", handle_letter_check),
        "5": ("Форматирование чисел", handle_number_formatting),
        "6": ("Очистка текста", handle_clean_text),
        "7": ("Средняя длина слова", handle_average_word_length),
        "8": ("Поиск максимумов", handle_max_values),
        "9": ("Уникальные символы", handle_unique_chars),
        "10": ("Частота слов", handle_word_frequency),
        # Импорт модуля целиком
        "11": ("Сложная фильтрация слов", word_filter.handle_word_filter),
        "12": ("Среднее арифметическое", average_calc.handle_average),
        "13": ("Обработка текста", text_processor.handle_text_processing),
        "14": ("Map и лямбда (квадраты и минусы)", map_lambda_range.handle_map_lambda_range),
        "15": ("Число Фибоначчи", fibonacci.handle_fibonacci),
        "16": ("Своя реализация map", my_map.handle_my_map),
        "17": ("Своя реализация filter", my_filter.handle_my_filter),
        "18": ("Фибоначчи с декоратором кэша", decorator_cache.handle_fibonacci_decorated),
        "19": ("Декоратор repeat_deco", decorator_repeat.handle_repeat_decorator),
        "20": ("Демонстрация global", global_var.handle_global_var),
        "21": ("Демонстрация nonlocal", nonlocal_var.handle_nonlocal_var),

    }

    while True:
        print("\n--- Меню ---")
        for key, (title, _) in menu.items():
            print(f"{key}. {title}")
        print("0. Выход")

        choice = input("Выбор: ").strip()

        if choice == "0":
            print("Пока.")
            break
        if choice in menu:
            menu[choice][1]()
        else:
            print("Нет такого пункта, попробуйте снова.")


if __name__ == "__main__":
    main()