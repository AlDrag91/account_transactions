from src.utils import *


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
