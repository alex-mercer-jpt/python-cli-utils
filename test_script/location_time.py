


"""
Модуль для вывода текущей локации и времени.
Запрашивает у пользователя город и время, затем выводит их в заданном формате.
"""


def handle_location_time() -> None:
    """
    Запрашивает город и время, выводит строку в формате:
    'Current location is {city} and time is {time}'.

    Если хотя бы одно поле оставлено пустым, выводит сообщение об ошибке.
    """
    user_city = input("Введите город: ").strip()
    user_time = input("Введите время: ").strip()

    if not user_city or not user_time:
        print("Город или Время не введены")
        return

    print(f"Current location is {user_city} and time is {user_time}")


