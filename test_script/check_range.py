



"""
Модуль для проверки чисел на принадлежность к диапазону.
Считывает границы, затем числа до пустой строки и проверяет, все ли они внутри.
"""


def handle_check_range() -> None:
    """
    Запрашивает левую и правую границы (целые числа).
    Затем в цикле считывает числа (пустая строка — завершение).
    Выводит True, если ВСЕ введенные числа строго внутри диапазона, иначе False.
    """
    try:
        left = int(input("Левая граница: "))
        right = int(input("Правая граница: "))
    except ValueError:
        print("Ошибка: границы должны быть целыми числами.")
        return

    all_ok = True
    print("Вводите числа (пустая строка — завершить):")

    # Используем walrus operator (моржовый оператор) для лаконичности
    while data := input():
        try:
            number = int(data)
        except ValueError:
            print(f"  '{data}' — не число, пропускаю.")
            continue

        # Если число вышло за границы, меняем флаг
        if number <= left or number >= right:
            all_ok = False

    print(f"Все числа внутри диапазона: {all_ok}")


if __name__ == "__main__":
    # Изолированный запуск для проверки: python check_range.py
    handle_check_range()