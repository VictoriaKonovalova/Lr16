def listt(trains):
    """
        Отобразить список маршрутов
    """
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех маршрутах
        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    train.get('name', ''),
                    train.get('num', ''),
                    train.get('time', 0)
                )
            )

        print(line)
    else:
        print("Список маршрутов пуст!")
