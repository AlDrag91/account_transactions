import json
from datetime import datetime


def get_data_operations():
    """Получение данных"""
    with open("operations.json", "r", encoding='utf-8') as fail:
        data = json.load(fail)
    return data


def remove_data_voids(data):
    """Удаление пустых элементов из загруженного файла"""
    return [i for i in data if "date" in i]


def filter_status(data):
    """Фильтрация стратуса перевода"""
    return [i for i in data if i['state'] == "EXECUTED"]


def sort_dates(data):
    """Сортировка данных по дате"""
    data = sorted(data, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return data


def get_first_data(data, number_last):
    """Возвращает первые значения"""
    return data[:number_last]


def get_processing_data(number_last):
    get_data = get_data_operations()
    remove_voids_data = remove_data_voids(get_data)
    executed_data = filter_status(remove_voids_data)
    sort_dates_data = sort_dates(executed_data)
    ready_data = get_first_data(sort_dates_data, number_last)

    return ready_data
