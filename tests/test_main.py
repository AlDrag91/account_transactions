from unittest.mock import patch

from src.main import *


def test_format_date():
    assert format_date({"date": "2019-07-13T18:51:29.313309"}) == "13.07.2019"


def test_hide_data(mocked_data_flag_to, mocked_data_flag_from):
    assert hide_data("Счет 43241152692663622869", "to") == mocked_data_flag_to
    assert hide_data("Maestro 7810846596785568", "from") == mocked_data_flag_from


def test_output_format(mocked_flag_to_from, mocked_data_flag_to, mocked_result_flag_to, mocked_data_flag_from, mocked_result_flag_from):
    result = output_format(mocked_flag_to_from, "19.11.2019", mocked_data_flag_to)
    assert result.strip() == mocked_result_flag_to.strip()
    result = output_format(mocked_flag_to_from, "19.11.2019", mocked_data_flag_to, mocked_data_flag_from)
    assert result.strip() == mocked_result_flag_from.strip()


def test_main(mocked_data_result, mocked_result_flag_to, mocked_data_flag_to):
    with patch("src.main.get_processing_data", return_value=mocked_data_result):
        with patch("src.main.format_date", return_value="19.11.2019"):
            with patch("src.main.hide_data", return_value=mocked_data_flag_to):
                with patch("src.main.output_format", return_value=mocked_result_flag_to):
                    results = main(5)
                    assert results == [mocked_result_flag_to] * 5
