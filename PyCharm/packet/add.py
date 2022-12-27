def add(trains, name, num, time):
    """
        Добавляем маршруты
    """
    # Создать словарь
    train = {
        'name': name,
        'num': num,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('num', ''))
