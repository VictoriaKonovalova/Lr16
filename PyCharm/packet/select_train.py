def select_train(trains, number):
    """""
    Выбрать маршруты с заданным номер поезда
    """""
    # Сформировать список поездов
    result = []
    for rattler in trains:
        if rattler.get('num') == number:
            result.append(rattler)

    # Возвратить список выбранных маршрутов
    return result
