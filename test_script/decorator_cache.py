



"""
Модуль для демонстрации декоратора кэширования (мемоизации).
Кэширует результаты функции, чтобы не вычислять их повторно.
"""


def cache_deco(func):
    """
    Декоратор: кэширует результаты функции по аргументам.
    Использует словарь, где ключ — это аргументы (args и kwargs).
    """
    cache = {}
    def wrapper(*args, **kwargs):
        # Создаем уникальный ключ из позиционных и именованных аргументов
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]

        # Если ключа нет, вычисляем и сохраняем
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper


@cache_deco
def slow_fib(k: int) -> int:
    """
    Число Фибоначчи с рекурсией.
    Без кэша работает экспоненциально долго, с кэшем — мгновенно.
    """
    if k <= 2:
        return 1
    return slow_fib(k - 1) + slow_fib(k - 2)


def handle_fibonacci_decorated() -> None:
    """
    Обертка для меню: запрашивает номер и выводит число Фибоначчи,
    вычисленное с помощью декоратора кэширования.
    """
    print("--- Число Фибоначчи (с декоратором кэширования) ---")
    raw = input("Введите порядковый номер n (например, 30, максимум 450): ").strip()

    try:
        n = int(raw)
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return

    if n < 1:
        print("Ошибка: число должно быть положительным.")
        return

    if n > 450:
        print("Ошибка: из-за ограничений рекурсии в Python максимум 450.")
        return

    result = slow_fib(n)
    print(f"Результат: {result}")


if __name__ == "__main__":
    # Изолированный запуск для проверки: python decorator_cache.py
    handle_fibonacci_decorated()