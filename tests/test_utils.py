from unittest.mock import mock_open, patch
from src.utils import *


def test_get_data_operations(mocked_data_operations):
    mocked_data = json.dumps(mocked_data_operations)
    i = mock_open(read_data=mocked_data)
    with patch('builtins.open', i):
        result = get_data_operations()
    assert result == mocked_data_operations


def test_remove_date_voids(mocked_data_operations, mocked_remove_data_voids):
    assert remove_data_voids(mocked_data_operations) == mocked_remove_data_voids


def test_filter_status(mocked_data_sort, mocked_result_data):
    assert filter_status(mocked_data_sort) == mocked_result_data


def test_sort_dates(mocked_remove_data_voids, mocked_data_sort):
    assert sort_dates(mocked_remove_data_voids) == mocked_data_sort


def test_get_first_data(mocked_result_data, mocked_first_data):
    assert get_first_data(mocked_result_data, 5) == mocked_first_data


def test_get_processing_data(mocked_data_operations, mocked_remove_data_voids, mocked_data_sort, mocked_result_data,
                             mocked_first_data):
    with patch("src.utils.get_data_operations", return_value=mocked_data_operations):
        with patch("src.utils.remove_data_voids", return_value=mocked_remove_data_voids):
            with patch("src.utils.get_first_data", return_value=mocked_result_data):
                with patch("src.utils.sort_dates", return_value=mocked_data_sort):
                    with patch("src.utils.get_first_data", return_value=mocked_first_data):
                        assert get_processing_data(5) == mocked_first_data


def test_format_date():
    assert format_date({"date": "2019-07-13T18:51:29.313309"}) == "13.07.2019"


def test_hide_data(mocked_data_flag_to, mocked_data_flag_from):
    assert hide_data("Счет 43241152692663622869", "to") == mocked_data_flag_to
    assert hide_data("Maestro 7810846596785568", "from") == mocked_data_flag_from


def test_output_format(mocked_flag_to_from, mocked_data_flag_to, mocked_result_flag_to, mocked_data_flag_from,
                       mocked_result_flag_from):
    result = output_format(mocked_flag_to_from, "19.11.2019", mocked_data_flag_to)
    assert result.strip() == mocked_result_flag_to.strip()
    result = output_format(mocked_flag_to_from, "19.11.2019", mocked_data_flag_to, mocked_data_flag_from)
    assert result.strip() == mocked_result_flag_from.strip()
