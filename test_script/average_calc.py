



"""
Модуль для вычисления среднего арифметического числа.
Считывает строки с числами до пустой строки и выводит среднее для каждой.
"""


def calculate_average(numbers: str) -> float | None:
    """
    Вычисляет среднее арифметическое чисел в строке.
    Возвращает округленное значение до 2 знаков или None, если строка пуста.
    """
    nums = [int(x) for x in numbers.split()]
    if not nums:
        return None
    return round(sum(nums) / len(nums), 2)


def handle_average() -> None:
    """
    Обертка для меню: читает строки с числами до пустой строки,
    вызывает calculate_average и печатает результат.
    """
    print("--- Вычисление среднего арифметического ---")
    print("Вводите числа через пробел (пустая строка — завершить):")

    # walrus operator (:=) позволяет одновременно присвоить и проверить на пустоту
    while data := input("> "):
        result = calculate_average(data)
        if result is None:
            print("Пустой ввод, пропускаю.")
        else:
            print(f"Среднее: {result}")

