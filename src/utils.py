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
    """Возвращаем указанное кол-во данных с сортировкой по дате и статосу"""
    get_data = get_data_operations()
    remove_voids_data = remove_data_voids(get_data)
    executed_data = filter_status(remove_voids_data)
    sort_dates_data = sort_dates(executed_data)
    ready_data = get_first_data(sort_dates_data, number_last)

    return ready_data


def format_date(data):
    """Форматирование даты"""
    date_result = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date_result


def hide_data(data, r):
    """Функция для маскировки счета"""
    p = data.split()
    length_account = p[-1]
    if r == 'form':
        if 'Счет' in p:
            hide_nambe = ' ' + '**' + length_account[-4:]
        else:
            hide_nambe = length_account[:4] + ' ' + length_account[4:6] + '**' + ' ' + '****' + ' ' + length_account[
                                                                                                      -4:]
    else:
        if 'Счет' in p:
            hide_nambe = ' ' + '**' + length_account[-4:]
        else:
            hide_nambe = length_account[:4] + ' ' + length_account[4:6] + '**' + ' ' + '****' + ' ' + length_account[
                                                                                                      -4:]

    return ' '.join(p[:-1] + [hide_nambe])


def output_format(data, result_date, flag_to, flag_from=None):
    """Формирование результата"""
    date_and_method = f"{result_date} {data['description']}"
    transaction_operation = flag_from and f"{flag_from} -->> {flag_to}" or flag_to
    quantity = f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"
    return f"{date_and_method}\n{transaction_operation}\n{quantity}"
