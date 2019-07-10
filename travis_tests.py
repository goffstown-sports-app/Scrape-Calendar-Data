import unittest
import utility_functions as UF
import datetime
import calendar_functions as CF


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
        datetime_result = UF.check_type(datetime.datetime(2019, 6, 12), "datetime")
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

    ###############################################
    #Testing the functions in calendar_functions.py#
    ###############################################

    def test_get_events_for_day(self):
        """
        Tests the get_events_for_day function 
        """
        single_content_response = CF.get_events_for_day(4, 6, 2019)
        double_content_response = CF.get_events_for_day(6, 6, 2019)
        zero_content_response = CF.get_events_for_day(8, 6, 2019)

        self.assertEqual(single_content_response, [{'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Volleyball', 'eventid': 75486571, 'isPostponed': 0, 'thedate': '(H) 6:00PM vs Pinkerton Academy', 'homeOrAway': 1, 'postcancelled': '', 'eventType': 'home', 'Year': 2019, 'thePlace': '@ GHS Gymnasium', 'rescheddate': '', 'Day': 4, 'theEventTitle': 'NHIAA Playoff Quarterfinal'}])

        self.assertEqual(double_content_response, [{'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Volleyball', 'eventid': 75496026, 'isPostponed': 0, 'thedate': '(A) 5:00PM vs Salem Athletics', 'homeOrAway': 0, 'postcancelled': '', 'eventType': 'away', 'Year': 2019, 'thePlace': '@ Nashua North High School', 'rescheddate': '', 'Day': 6, 'theEventTitle': 'NHIAA Semifinals'}, {'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Lacrosse', 'eventid': 75507003, 'isPostponed': 0, 'thedate': '(H) 7:15PM vs Derryfield School', 'homeOrAway': 1, 'postcancelled': '', 'eventType': 'home', 'Year': 2019, 'thePlace': '@ Stellos Stadium', 'rescheddate': '', 'Day': 6, 'theEventTitle': 'NHIAA Semifinals'}])

        self.assertEqual(zero_content_response, None)

    def test_cleaning_response(self):
        """
        Testing the cleaning_response function
        """
        single_content_response = CF.cleaning_response(CF.get_events_for_day(4, 6, 2019), 4, 6, 2019)
        double_content_response = CF.cleaning_response(CF.get_events_for_day(6, 6, 2019), 6, 6, 2019)
        zero_content_response = CF.cleaning_response(CF.get_events_for_day(8, 6, 2019), 8, 6, 2019)

        self.assertEqual(single_content_response, [{'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': True, 'location': 'GHS Gymnasium', 'start-time-(normal)': '6:00PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 4, 18, 0), 'hour': 18, 'minute': 0, 'away_team_name': 'Pinkerton Academy', 'sport': 'Volleyball', 'cancelled': False}])

        self.assertEqual(double_content_response, [{'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': False, 'location': 'Nashua North High School', 'start-time-(normal)': '5:00PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 6, 17, 0), 'hour': 17, 'minute': 0, 'away_team_name': 'Salem Athletics', 'sport': 'Volleyball', 'cancelled': False}, {'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': True, 'location': 'Stellos Stadium', 'start-time-(normal)': '7:15PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 6, 19, 15), 'hour': 19, 'minute': 15, 'away_team_name': 'Derryfield School', 'sport': 'Lacrosse', 'cancelled': False}])

        self.assertEqual(zero_content_response, None)


if __name__ == '__main__':
    unittest.main()
