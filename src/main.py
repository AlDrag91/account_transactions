from src.utils import *
import datetime
from datetime import datetime


def format_date(data):
    """Форматирование даты"""
    date_result = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date_result


def hide_data(data, r):
    """Скрывает символы в номере счета"""
    p = data.split()
    length_account = p[-1]
    if r == 'form':
        hide_nambe = length_account[:4] + ' ' + length_account[4:6] + '**' + ' ' + '****' + ' ' + length_account[-4:]
    else:
        hide_nambe = length_account[:4] + ' ' + '****' + ' ' + '****' + ' ' + length_account[-4:]
    return ' '.join(p[:-1] + [hide_nambe])


def output_format(data, result_date, flag_to, flag_from=None):
    """Формирование результата"""
    date_and_method = f"{result_date} {data['description']}"
    transaction_operation = flag_from and f"{flag_from} -->> {flag_to}" or flag_to
    quantity = f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}"
    return f"{date_and_method}\n{transaction_operation}\n{quantity}"


def main(number_list):
    datas = get_processing_data(number_list)
    final_result = []
    for data in datas:
        result_date = format_date(data)
        flag_to = hide_data(data['to'], 'from')
        flag_from = None
        if "from" in data:
            flag_from = hide_data(data['from'], "from")
        results_data = output_format(data, result_date, flag_to, flag_from)
        final_result.append(results_data)
    return final_result


if __name__ == '__main__':
    for upshot in main(5):
        print(upshot + '\n')
