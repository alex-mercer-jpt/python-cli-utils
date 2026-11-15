


"""
Модуль для демонстрации декоратора repeat_deco.
Повторяет вызов функции n раз и возвращает результат последнего вызова.
"""


def repeat_deco(n=1):
    """
    Декоратор: повторяет вызов декорированной функции n раз.
    Возвращает значение из последнего вызова.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def handle_repeat_decorator() -> None:
    """
    Обертка для меню: демонстрирует работу декоратора repeat_deco
    в двух режимах (вывод в столбик и сбор в список).
    """
    print("--- Демонстрация repeat_deco ---")

    # 1. Спрашиваем количество повторений
    raw_n = input("Сколько раз повторить? (например, 4): ").strip()
    try:
        n = int(raw_n)
        if n < 1:
            print("Ошибка: нужно число больше 0.")
            return
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return

    # 2. Спрашиваем, ЧТО повторять
    user_input = input("Что будем повторять? (можно ввести любое слово, число или фразу, например: 'hello', '123', 'hello 123'): ").strip()

    # 3. Спрашиваем, КАК выводить
    print("\nВыберите режим:")
    print("1. Вывести в столбик (каждое значение с новой строки)")
    print("2. Собрать в список и вывести в строку (как массив)")
    mode = input("Ваш выбор (1 или 2): ").strip()

    if mode == "1":
        print("\n--- Вывод в столбик ---")
        @repeat_deco(n)
        def action():
            print(user_input)
        action()

    elif mode == "2":
        print("\n--- Вывод в строку ---")
        @repeat_deco(n)
        def action(seq, val):
            seq.append(val)
            return seq

        # Умная проверка: если ввели только цифры, превращаем в int
        if user_input.isdigit():
            val_to_add = int(user_input)
        else:
            val_to_add = user_input

        result = action([], val_to_add)
        print(f"Результат: {result}")

    else:
        print("Неверный режим.")


