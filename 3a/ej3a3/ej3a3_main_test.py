from ej3a3_time_package import *
import datetime
from flake8.api import legacy as flake8


# archivo: test_arithmetic.py
def test_convert_date_format():
    assert convert_date_format.string_to_datetime("2024-05-01") == datetime.datetime(
        2024, 5, 1, 0, 0
    ), "string_to_datetime does not return the correct value for input '2024-05-01'. It should be datetime.datetime(2024, 5, 1, 0, 0)"
    assert (
        convert_date_format.datetime_to_string(datetime.datetime(2024, 5, 1, 0, 0))
        == "2024-05-01"
    ), "datetime_to_string does not return the correct value for input datetime.datetime(2024, 5, 1, 0, 0). It should be '2024-05-01'"
    assert (
        convert_date_format.datetime_to_string(
            datetime.datetime(2024, 5, 1, 0, 0), "%m-%d"
        )
        == "05-01"
    ), "datetime_to_string does not return the correct value for input datetime.datetime(2024, 5, 1, 0, 0), '%m-%d'. It should be '05-01'"


def test_date_operations():
    assert date_operations.add_days(
        datetime.datetime(2024, 5, 1, 0, 0), 10
    ) == datetime.datetime(2024, 5, 11, 0, 0), "add_days does not return the correct value for input datetime.datetime(2024, 5, 1, 0, 0), 10. It should be datetime.datetime(2024, 5, 11, 0, 0)"
    assert date_operations.middle_day_between_two_dates(
        datetime.datetime(2024, 5, 1, 0, 0), datetime.datetime(2024, 5, 11, 0, 0)
    ) == datetime.datetime(2024, 5, 6, 0, 0), "middle_day_between_two_dates does not return the correct value for input datetime.datetime(2024, 5, 1, 0, 0), datetime.datetime(2024, 5, 11, 0, 0). It should be datetime.datetime(2024, 5, 6, 0, 0)"


def test_pep8_conformity():
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files([
        "ej3a3_main.py", 
        "ej3a3_time_package/"
    ])
    
    assert report.get_statistics("") == [], (
        "Your code does not comply with flake8. Please review your code"
    )
