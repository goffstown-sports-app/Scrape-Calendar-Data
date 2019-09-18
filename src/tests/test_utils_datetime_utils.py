import sys

sys.path.append("..")
from utils import datetime_utils


def test_normal_time_to_datetime(self):
    """
    Tests the normal_time_to_ISO function
    """
    am_test = datetime_utils.normal_time_to_datetime("5:23AM", 6, 2, 2019)
    pm_test = datetime_utils.normal_time_to_datetime("7:45PM", 4, 9, 2019)
    assert str(type(am_test)) == "<class 'datetime.datetime'>"
    assert str(type(pm_test)) == "<class 'datetime.datetime'>"
    assert am_test.year == 2019
    assert am_test.month == 2
    assert am_test.day == 6
    assert am_test.hour == 5
    assert am_test.minute == 23
    assert pm_test.year == 2019
    assert pm_test.month == 9
    assert pm_test.day == 4
    assert pm_test.hour == 19
    assert pm_test.minute == 45
