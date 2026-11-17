



"""
Модуль для подсчета частоты слов в тексте.
Находит самое частое слово и выводит его вместе с количеством повторений.
"""


def handle_word_frequency() -> None:
    """
    Запрашивает текст, считает частоту слов (без учета регистра)
    и выводит самое частое слово и сколько раз оно встретилось.
    """
    print("--- Подсчет частоты слов ---")
    text_user = input("Введите текст: ").lower().split()

    if not text_user:
        print("Ошибка: текст не введен или пуст.")
        return

    # Считаем частоту слов
    counts: dict[str, int] = {}
    for word in text_user:
        counts[word] = counts.get(word, 0) + 1  # Более компактная запись, чем if/else

    # Находим самое частое слово (max по значению словаря)
    most_common = max(counts, key=counts.get)
    count = counts[most_common]

    # Для меню выводим красиво:
    print(f"Самое частое слово: '{most_common}' (встречается {count} раз(а))")


