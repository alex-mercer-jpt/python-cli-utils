


"""
Модуль для демонстрации работы ключевого слова nonlocal.
Показывает, как вложенная функция может изменять переменную
из объемлющей (внешней) области видимости.
"""


def create_multiplier(factor: int):
    """Внешняя функция. Создает функцию-умножитель."""
    # Локальная переменная внешней функции
    last_result = 0

    def multiplier(num: int) -> int:
        """Внутренняя функция. Использует nonlocal."""
        nonlocal last_result
        # Мы меняем переменную из внешней функции!
        last_result = num * factor
        return last_result

    return multiplier


def handle_nonlocal_var() -> None:
    """Обертка для меню."""
    print("Создаем функцию-умножитель на 2.")
    times_two = create_multiplier(2)

    try:
        num1 = int(input("Введите первое число: "))
        res1 = times_two(num1)
        print(f"Результат: {res1}")

        num2 = int(input("Введите второе число: "))
        res2 = times_two(num2)
        print(f"Результат: {res2}")

        print("Как видите, внутренняя функция запомнила, что она умножает на 2.")
    except ValueError:
        print("Ошибка ввода.")