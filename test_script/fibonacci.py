


"""
Модуль для вычисления чисел Фибоначчи с помощью рекурсии и кэширования.
Использует необязательный аргумент cache для хранения уже вычисленных значений.
"""


def fibonacci(n: int, cache: dict[int, int] | None = None) -> int:
    """
    Вычисляет n-е число Фибоначчи (1, 1, 2, 3, 5, ...).
    cache — необязательный аргумент для кэширования (мемоизации).
    """
    if cache is None:
        cache = {}
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]

    result = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = result
    return result


def handle_fibonacci() -> None:
    """
    Обертка для меню: запрашивает n и выводит n-е число Фибоначчи.
    """
    print("--- Вычисление числа Фибоначчи ---")
    raw = input("Введите порядковый номер n (1..450): ").strip()

    if not raw.isdigit():
        print("Ошибка: нужно положительное целое число.")
        return

    n = int(raw)
    if not (1 <= n <= 450):
        print("Ошибка: n должно быть от 1 до 450.")
        return

    result = fibonacci(n)
    print(f"Число Фибоначчи под номером {n}: {result}")


if __name__ == "__main__":
    # Изолированный запуск для проверки: python fibonacci.py
    handle_fibonacci()