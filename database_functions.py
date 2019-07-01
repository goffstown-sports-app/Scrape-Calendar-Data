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
    ref = db.refernce("field_information")
    child_ref = ref.child("general-information")
    child_ref.set({
        "events-so-far": 0,
        "total-events-today": 0,
        "total-events-today-list": [],
        "active-events": 0,
        "active-events-list": []
    })
    for field in list_of_field_names:
        field_ref = ref.child("field-status/" + field)
        field_ref.set({
            "last-update": str(datetime.now()),
            "sport": "",
            "start-time": "00:00:00",
            "end-time": "00:00:00",
            "away-team-name": "",
            "varsity-sport": False
        })
    print("created/reset field_information section in realtime database")


# Testing:
init_field_information_section([
    "softball-field",
    "baseball-field",
    "gym",
    "football-field",
    "jv-field"
])