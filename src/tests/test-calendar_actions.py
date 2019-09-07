import datetime
import unittest
import sys

sys.path.append("..")
import calendar_actions as CA


class UnitTest(unittest.TestCase):
    """
    Will run unittests for the calendar_actions.py file
    """

    def test_get_events_for_day(self):
        """
        Tests the get_events_for_day function
        """
        single_content_response = CA.get_events_for_day(4, 6, 2019)
        double_content_response = CA.get_events_for_day(6, 6, 2019)
        zero_content_response = CA.get_events_for_day(8, 6, 2019)

        self.assertEqual(single_content_response, [{'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Volleyball', 'eventid': 75486571, 'isPostponed': 0, 'thedate': '(H) 6:00PM vs Pinkerton Academy', 'homeOrAway': 1, 'postcancelled': '', 'eventType': 'home', 'Year': 2019, 'thePlace': '@ GHS Gymnasium', 'rescheddate': '', 'Day': 4, 'theEventTitle': 'NHIAA Playoff Quarterfinal'}])

        self.assertEqual(double_content_response, [{'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Volleyball', 'eventid': 75496026, 'isPostponed': 0, 'thedate': '(A) 5:00PM vs Salem Athletics', 'homeOrAway': 0, 'postcancelled': '', 'eventType': 'away', 'Year': 2019, 'thePlace': '@ Nashua North High School', 'rescheddate': '', 'Day': 6, 'theEventTitle': 'NHIAA Semifinals'}, {'isAuthorized': True, 'isCancelled': 0, 'Month': 6, 'theTitle': 'Boys Varsity Lacrosse', 'eventid': 75507003, 'isPostponed': 0, 'thedate': '(H) 7:15PM vs Derryfield School', 'homeOrAway': 1, 'postcancelled': '', 'eventType': 'home', 'Year': 2019, 'thePlace': '@ Stellos Stadium', 'rescheddate': '', 'Day': 6, 'theEventTitle': 'NHIAA Semifinals'}])

        self.assertEqual(zero_content_response, None)

    def test_cleaning_response(self):
        """
        Testing the cleaning_response function
        """
        single_content_response = CA.cleaning_response(
            CA.get_events_for_day(4, 6, 2019), 4, 6, 2019)
        double_content_response = CA.cleaning_response(
            CA.get_events_for_day(6, 6, 2019), 6, 6, 2019)
        zero_content_response = CA.cleaning_response(
            CA.get_events_for_day(8, 6, 2019), 8, 6, 2019)

        self.assertEqual(single_content_response, [{'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': True, 'location': 'GHS-GYM-FIELD', 'start-time-(normal)': '6:00PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 4, 18, 0), 'hour': 18, 'minute': 0, 'away_team_name': 'Pinkerton Academy', 'sport': 'Volleyball', 'cancelled': False}])

        self.assertEqual(double_content_response, [{'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': False, 'location': 'Nashua North High School', 'start-time-(normal)': '5:00PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 6, 17, 0), 'hour': 17, 'minute': 0, 'away_team_name': 'Salem Athletics', 'sport': 'Volleyball', 'cancelled': False}, {'gender': 'm', 'varsity': True, 'ghs_sport': True, 'home': True, 'location': 'GHS-FOOTBALL-FIELD', 'start-time-(normal)': '7:15PM', 'stat-time-(datetime)': datetime.datetime(2019, 6, 6, 19, 15), 'hour': 19, 'minute': 15, 'away_team_name': 'Derryfield School', 'sport': 'Lacrosse', 'cancelled': False}])

        self.assertEqual(zero_content_response, None)


if __name__ == '__main__':
    unittest.main()
