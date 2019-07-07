import database_functions as DF
import calendar_functions as CF
from datetime import datetime
from time import sleep
import firebase_admin
from firebase_admin import credentials


def main():
    """
    Runs main
    """
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com/"})
    while True:
        datetime_now = datetime.now()
        day = int(datetime_now.day)
        month = int(datetime_now.month)
        year = int(datetime_now.year)
        inital_response = CF.get_events_for_day(day, month, year)
        print(inital_response)
        cleaned_response = CF.cleaning_response(inital_response, day, month, year)
        print(cleaned_response)
        if cleaned_response != None:
            hour = int(datetime_now.hour)
            DF.update_database(cleaned_response, hour)
        elif cleaned_response == None:
            print("Nothing right now, database not updated")
        sleep(180)


main()
