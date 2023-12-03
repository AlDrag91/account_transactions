import pytest


@pytest.fixture
def mocked_data_operations():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689"
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {},
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }

    ]


@pytest.fixture
def mocked_remove_data_voids():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }

    ]


@pytest.fixture
def mocked_data_sort():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }
    ]


@pytest.fixture
def mocked_result_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        },
        {
            "state": "EXECUTED",
            "date": "2018-06-19T09:22:25.899614"
        }
    ]


@pytest.fixture
def mocked_first_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614"
        },
        {
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
        }
    ]


@pytest.fixture
def mocked_data_flag_to():
    return "Счет  **2869"


@pytest.fixture
def mocked_flag_to_from():
    return {
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869"
    }


@pytest.fixture
def mocked_result_flag_to():
    return """
    19.11.2019 Перевод организации\nСчет  **2869\n30153.72 руб.
    """


@pytest.fixture
def mocked_data_flag_from():
    return "Maestro 7810 **** **** 5568"


@pytest.fixture
def mocked_result_flag_from():
    return """
    19.11.2019 Перевод организации\nMaestro 7810 **** **** 5568 -->> Счет  **2869\n30153.72 руб.
    """


@pytest.fixture
def mocked_data_result():
    return [{
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869"
    }] * 5
