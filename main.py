from datetime import datetime
from time import sleep
import firebase_admin
from firebase_admin import credentials
import json
from os import system

import database
import calendar_actions as CA


def main():
    """
    Runs main
    :return: none
    """
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com/"})
    number_of_requests = 1
    print("20 seconds till start")
    sleep(20)
    while True:
        try:
            database.update_pulse(number_of_requests)
            datetime_now = datetime.now()
            day = int(datetime_now.day)
            month = int(datetime_now.month)
            year = int(datetime_now.year)
            hour = int(datetime_now.hour)
            minute = int(datetime_now.minute)
            initial_response = CA.get_events_for_day(day, month, year)
            cleaned_response = CA.cleaning_response(
                initial_response, day, month, year)
            if hour == 0 and minute <= 3:
                database.init_database([
                    "V-M-Soccer",
                    "JV-M-Soccer",
                    "V-F-Soccer",
                    "JV-F-Soccer",
                    "V-M-Football",
                    "JV-M-Football",
                    "V-M-Baseball",
                    "JV-M-Baseball",
                    "V-F-Softball",
                    "JV-F-Softball",
                    "V-F-Field_Hockey",
                    "JV-F-Field_Hockey",
                    "V-M-Volleyball",
                    "JV-M-Volleyball",
                    "V-F-Volleyball",
                    "JV-F-Volleyball",
                    "V-M-Basketball",
                    "JV-M-Basketball",
                    "V-F-Basketball",
                    "JV-F-Basketball",
                    "V-M-Lacrosse",
                    "JV-M-Lacrosse",
                    "V-F-Lacrosse",
                    "JV-F-Lacrosse"
                ])
                database.init_calendar_section()
                database.init_field_information_section([
                    "softball-field",
                    "gym",
                    "football-field"
                ])
                system("rm request_data.json")
            print("")
            first_time_run = 0
            if cleaned_response != None:
                database.update_database(cleaned_response, hour)
                database.update_calendar_section(cleaned_response)
                print("Updated database\nNext check in 3 min\n")
                first_time_run += 1
                saved_description = "wrote data"
            else:
                print("Didn't update database\nNext check in 3 min\n")
                saved_description = "nothing"
                first_time_run += 1
            if first_time_run == 0:
                with open("request_data.json", "w") as request_data:
                    json.dump([], request_data)
            with open("request_data.json", "a") as request_data:
                json.dump([str(datetime_now), saved_description], request_data)
            for i in range(180):
                sleep(1)
                print("\n--------------------------------")
                print(180 - i, "seconds till next request")
                print("\nNumber of request:", number_of_requests)
            for i in range(40):
                print("\n")
            print("Making request")
            number_of_requests += 1
        except:
            print("Error in program.")
            print("Retrying")
            for i in range(10):
                sleep(1)
                print("\n--------------------------------")
                print(10 - i, "seconds till retry")
            for i in range(40):
                print("\n")


if __name__ == "__main__":
    main()
