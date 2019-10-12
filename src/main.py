from datetime import datetime
from time import sleep
import firebase_admin
from firebase_admin import credentials
from os import system
from ghsTools import ghsTools

import database
import calendar_actions as CA


def main():
    """
    Runs main
    :return: none
    """
    cred = credentials.Certificate("./secrets/firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    number_of_requests = 1
    while True:
        time_diff = 180
        ghsTools().update_pulse(number_of_requests, "Scrape-Calendar-Data")
        ghsTools().set_monitoring_info(True, time_diff, "Scrape-Calendar-Data")
        datetime_now = datetime.now()
        print("Making request")
        initial_response = CA.get_events_for_day(
            datetime_now.day, datetime_now.month, datetime_now.year)
        print(initial_response,"\n")
        cleaned_response = CA.cleaning_response(
            initial_response, datetime_now.day, datetime_now.month, datetime_now.year)
        print(cleaned_response, "\n")
        if datetime_now.hour == 0 and datetime_now.minute <= time_diff / 60:
            database.init_calendar_section()
            database.init_field_information_section([
                "softball-field",
                "gym",
                "football-field"
            ])
        if cleaned_response != None:
            database.update_status_database(cleaned_response, datetime_now.hour)
            database.update_calendar_section(cleaned_response)
        number_of_requests += 1
        sleep(time_diff)


if __name__ == "__main__":
    main()
