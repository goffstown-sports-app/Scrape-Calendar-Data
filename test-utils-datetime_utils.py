import unittest

from src.utils import datetime_utils


class TestDatetimeUtils(unittest.TestCase):
    """
    Will run unittests for the src/utils/datetime_utils.py file
    """

    def test_normal_time_to_datetime(self):
        """
        Tests the normal_time_to_ISO function
        """
        am_test = datetime_utils.normal_time_to_datetime("5:23AM", 6, 2, 2019)
        pm_test = datetime_utils.normal_time_to_datetime("7:45PM", 4, 9, 2019)
        self.assertEqual(str(type(am_test)), "<class 'datetime.datetime'>")
        self.assertEqual(str(type(pm_test)), "<class 'datetime.datetime'>")
        self.assertEqual(am_test.year, 2019)
        self.assertEqual(am_test.month, 2)
        self.assertEqual(am_test.day, 6)
        self.assertEqual(am_test.hour, 5)
        self.assertEqual(am_test.minute, 23)
        self.assertEqual(pm_test.year, 2019)
        self.assertEqual(pm_test.month, 9)
        self.assertEqual(pm_test.day, 4)
        self.assertEqual(pm_test.hour, 19)
        self.assertEqual(pm_test.minute, 45)


if __name__ == '__main__':
    unittest.main()
