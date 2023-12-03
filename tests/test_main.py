from unittest.mock import patch

from src.main import *


def test_main(mocked_data_result, mocked_result_flag_to, mocked_data_flag_to):
    with patch("src.main.get_processing_data", return_value=mocked_data_result):
        with patch("src.main.format_date", return_value="19.11.2019"):
            with patch("src.main.hide_data", return_value=mocked_data_flag_to):
                with patch("src.main.output_format", return_value=mocked_result_flag_to):
                    results = main(5)
                    assert results == [mocked_result_flag_to] * 5
