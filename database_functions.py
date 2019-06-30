import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import utility_functions as UF
from datetime import datetime
import json


def upload_day_events(home, sport_name, cancelled, postponed, event_time, away_team_name, location, event_name, event_number):
    """
    Uploads all the events for the day to the Realtime database
    :param home: event is home (bool)
    :param sport_name: name of the sport (str)
    :param cancelled: if event is cancelled (bool)
    :param postponed: if event is postponed (bool)
    :param event_time: time of event (str)
    :param away_team_name: name of the away team (str)
    :param location: name of the location (str)
    :param event_name: name of the event (str)
    :param event_number: number of event (int)
    :return: none
    """
    # Type Checking:
    UF.check_type(home, "bool")
    UF.check_type(sport_name, "str")
    UF.check_type(cancelled, "bool")
    UF.check_type(postponed, "bool")
    UF.check_type(event_time, "str")
    UF.check_type(away_team_name, "str")
    UF.check_type(location, "str")
    UF.check_type(event_name, "str")
    UF.check_type(event_number, "int")

    # Data manipulation:
    datetime_now = datetime.now()
    current_year = datetime_now.year
    current_month = datetime_now.month
    current_day = datetime_now.day

    # Realtime Database interactions:
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com"})
    ref = db.reference("events")
    child_ref = ref.child("tday_events/event_" + str(event_number))
    child_ref.set({
        "current-year": current_year,
        "current-month": current_month,
        "current-day": current_day,
        "home": home,
        "sport-name": sport_name,
        "cancelled": cancelled,
        "postponed": postponed,
        "event_time": event_time,
        "away_team_name": away_team_name,
        "location": location,
        "event_name": event_name
    })