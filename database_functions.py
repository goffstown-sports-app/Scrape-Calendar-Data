import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import utility_functions as UF
from datetime import datetime


def init_field_information_section(list_of_field_names):
    """
    Initializes the field_information section of the realtime database
    :param list_of_field_names: list of all the field names
    :return: none
    """
    # Type checking:
    UF.check_type(list_of_field_names, "list")

    # Firebase interactions:
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com/"})
    ref = db.reference("field-information")
    child_ref = ref.child("general-information")
    child_ref.set({
        "events-so-far": 0,
        "total-events-today": 0,
        "active-events": 0,
    })
    for field in list_of_field_names:
        field_ref = ref.child("field-status/" + field)
        field_ref.set({
            "last-update": str(datetime.now()),
            "sport": "",
            "start-time": "00:00:00",
            "away-team-name": "",
            "varsity-sport": False
        })


# Testing:
# init_field_information_section([
#     "softball-field",
#     "gym",
#     "football-field",
#     "jv-field"
# ])


def update_database(cleaned_data):
    """
    Will update the database with information from the calendar.
    :param cleaned_data: clean data from the website
    :return: none
    """
    for event in cleaned_data:
        current_hour = datetime.now().hour
        event_hour = event["hour"]
        if current_hour == event_hour:
            if "gym" in event["location"].lower() and "ghs" in event["location"].lower() and event["home"]:
                field_name = "gym"
            elif "grizzles" in event["location"].lower() and "field" in event["location"].lower() and event["home"]:
                field_name = "football-field"
            elif "ghs" in event["location"].lower() and "softball" in event["location"].lower() and event["home"]:
                field_name = "softball-field"
            try:
                cred = credentials.Certificate("firestore_creds.json")
                firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com/"})
                ref = db.reference("field_information")
                child_ref = ref.child("field-information/" + field_name)
                child_ref.set({
                "last-update": str(datetime.now()),
                "sport": event["sport"],
                "start-time": event["start-time-(normal)"],
                "away-team-name": event["away_team_name"],
                "varsity-sport": event["varsity"]
                })
            except NameError:
                pass



