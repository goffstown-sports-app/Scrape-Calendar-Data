import database_functions as DF
import calendar_functions as CF
from datetime import datetime
from time import sleep
import firebase_admin
from firebase_admin import credentials
import json
from os import system


def main():
    """
    Runs main
    """
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com/"})
    while True:
        DF.update_pulse()
        datetime_now = datetime.now()
        day = int(datetime_now.day)
        month = int(datetime_now.month)
        year = int(datetime_now.year)
        hour = 0
        minute = 0
        inital_response = CF.get_events_for_day(day, month, year)
        cleaned_response = CF.cleaning_response(inital_response, day, month, year)
        if hour == 0 and minute <= 3:
            DF.init_database([
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
            DF.init_calendar_section()
            DF.init_field_information_section([
                "softball-field",
                "gym",
                "football-field"
            ])
            system("rm request_data.json")
        first_time_run = 0
        if cleaned_response != None:
            DF.update_database(cleaned_response, hour)
            DF.update_calendar_section(cleaned_response)
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
            print(180 - i, "seconds till next request")


if __name__ == "__main__":
    main()
