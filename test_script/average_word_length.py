

"""
Модуль для вычисления средней длины слова в тексте.
Словом считается любая последовательность символов, разделенная пробелами.
"""


def handle_average_word_length() -> None:
    """
    Запрашивает текст, разбивает на слова и выводит среднюю длину слова,
    округленную до 2 знаков после запятой.
    """
    print("--- Средняя длина слова в тексте ---")
    text = input("Введите текст (например, Hello World!): ").split()

    # Защита от пустого ввода (деления на ноль)
    if not text:
        print("Ошибка: текст не введен или пуст.")
        return

    # Считаем сумму длин всех слов и делим на их количество
    total_length = sum(len(word) for word in text)
    average = round(total_length / len(text), 2)

    print(f"Средняя длина слова: {average}")


if __name__ == "__main__":
    # Изолированный запуск для проверки: python average_word_length.py
    handle_average_word_length()