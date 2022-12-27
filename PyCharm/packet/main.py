from packet.add import add
from packet.listt import listt
from packet.select_train import select_train

import sys


def main():
    """
        Главная функция программы
    """
    # Сформировать список маршрутов
    route = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            add(route, name, num, time)

        elif command == 'list':
            listt(route)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            number = int(parts[1])
            selected = select_train(route, number)
            listt(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
