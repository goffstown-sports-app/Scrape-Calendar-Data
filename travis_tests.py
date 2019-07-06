import unittest
import utility_functions as UF
from datetime import datetime


class TravisTests(unittest.TestCase):
    """
    Will run unittests for functions.
    """

    ###############################################
    #Testing the functions in utility_functions.py#
    ###############################################

    def test_check_type(self):
        """
        Tests the check_type function
        """
        string_result = UF.check_type("", "string")
        int_result = UF.check_type(0, "int")
        float_result = UF.check_type(0.0, "float")
        tuple_result = UF.check_type((), "tuple")
        list_result = UF.check_type([], "list")
        dict_result = UF.check_type({}, "dict")
        bool_result = UF.check_type(True, "bool")
        datetime_result = UF.check_type(datetime(2019, 6, 12), "datetime")
        self.assertEqual(string_result, "<class 'str'>")
        self.assertEqual(int_result, "<class 'int'>")
        self.assertEqual(float_result, "<class 'float'>")
        self.assertEqual(tuple_result, "<class 'tuple'>")
        self.assertEqual(list_result, "<class 'list'>")
        self.assertEqual(dict_result, "<class 'dict'>")
        self.assertEqual(bool_result, "<class 'bool'>")
        self.assertEqual(datetime_result, "<class 'datetime.datetime'>")

    def test_normal_time_to_datetime(self):
        """
        Tests th normal_time_to_ISO function
        """
        am_test = UF.normal_time_to_datetime("5:23AM", 6, 2, 2019)
        pm_test = UF.normal_time_to_datetime("7:45PM", 4, 9, 2019)
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
