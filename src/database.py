from firebase_admin import db
from datetime import datetime

import utility as util


def init_field_information_section(list_of_field_names):
    """
    Initializes the field_information section of the realtime database
    :param list_of_field_names: list of all the field names
    :return: none
    """
    # Type checking:
    util.check_type(list_of_field_names, "list")

    # Firebase interactions:
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
            "sport": "",
            "start-time": "00:00:00",
            "away-team-name": "",
            "varsity-sport": False
        })


# Testing:
# init_field_information_section([
#     "softball-field",
#     "gym",
#     "football-field"
# ])


def update_database(cleaned_data, current_hour):
    """
    Will update the database with information from the calendar.
    :param cleaned_data: clean data from the website
    :param current_hour: the
    :return: none
    """
    got_data = 0
    for event in cleaned_data:
        event_hour = event["hour"]
        if current_hour == event_hour:
            if "gym" in event["location"].lower() and "ghs" in event["location"].lower() and event["home"]:
                field_name = "gym"
                got_data += 1
            elif "grizzles" in event["location"].lower() and "field" in event["location"].lower() and event["home"]:
                field_name = "football-field"
                got_data += 1
            elif "ghs" in event["location"].lower() and "softball" in event["location"].lower() and event["home"]:
                field_name = "softball-field"
                got_data += 1
            try:
                ref = db.reference("field-information")
                child_ref = ref.child("field-status/" + field_name)
                child_ref.set({
                    "sport": event["sport"],
                    "start-time": event["start-time-(normal)"],
                    "away-team-name": event["away_team_name"],
                    "varsity-sport": event["varsity"]
                })
            except NameError:
                pass


def init_calendar_section():
    """
    Initialize the calendar section of the database
    :return: none
    """
    ref = db.reference("calendar")
    child_ref = ref.child("tday-information")
    child_ref.set({"number-of-events": 0})
    for i in range(20):
        child_ref2 = ref.child("tday-events/event" + str(i))
        child_ref2.set({})


# Testing:
# init_calendar_section()


def update_calendar_section(list_of_events):
    """
    Update the database for the calendar section
    :param list_of_events: list of events for the day.
    :return: none
    """
    ref = db.reference("calendar")
    events = 0
    for event in list_of_events:
        events += 1
        child_ref = ref.child("tday-events/event" + str(events))
        child_ref.set({
            "location": event["location"],
            "sport": event["sport"],
            "start-time": event["start-time-(normal)"],
            "cancelled": event["cancelled"],
            "home": event["home"],
            "away-team": event["away_team_name"],
            "varsity": event["varsity"],
            "gender": event["gender"]
        })
    child_ref2 = ref.child("tday-information")
    child_ref2.set({"number-of-events": len(list_of_events)})


def init_database(list_of_sports):
    """
    Initializes the firebase realtime database
    :param list_of_sports: list of supported sports. Each sport should be marked like "V-M-Sport"
    :return: none
    """
    # Check types:
    util.check_type(list_of_sports, "list")
    for sport in list_of_sports:
        items = sport.split("-")
        if len(items) != 3:
            raise Exception(
                "It seems as though the sports came in wrong from the init_database function")
        if items[0].lower() != "v" and items[0].lower() != "jv":
            raise Exception(
                "It seems as though the varsity sports came in wrong for the init_database function")
        if items[1].lower() != "f" and items[1].lower() != "m":
            raise Exception(
                "Item seems as though the gender came in wrong for the init_database function")

    # Firestore interactions:
    ref = db.reference("scores")
    for sport in list_of_sports:
        items = sport.split("-")
        if items[0].lower() == "v":
            child_name = "varsity-scores/" + \
                items[1].upper() + "-" + items[2].lower()
        else:
            child_name = "jv-scores/" + \
                items[1].upper() + "-" + items[2].lower()
        child_ref = ref.child(child_name)
        child_ref.set({
            "home-score": 0,
            "away-score": 0,
            "game-time": "00:00:00",
            "period": 0,
            "away-team-name": "",
            "event-start": "",
            "event-end": ""
        })
    ref2 = db.reference("db-info")
    child_ref2 = ref2.child("pulses")
    current_time = datetime.now()
    child_ref2.set({
        "Scrape-Calendar-Pulse": str(current_time)
    })


# Testing:
# init_database([
#     "V-M-Soccer",
#     "JV-M-Soccer",
#     "V-F-Soccer",
#     "JV-F-Soccer",
#     "V-M-Football",
#     "JV-M-Football",
#     "V-M-Baseball",
#     "JV-M-Baseball",
#     "V-F-Softball",
#     "JV-F-Softball",
#     "V-F-Field_Hockey",
#     "JV-F-Field_Hockey",
#     "V-M-Volleyball",
#     "JV-M-Volleyball",
#     "V-F-Volleyball",
#     "JV-F-Volleyball",
#     "V-M-Basketball",
#     "JV-M-Basketball",
#     "V-F-Basketball",
#     "JV-F-Basketball",
#     "V-M-Lacrosse",
#     "JV-M-Lacrosse",
#     "V-F-Lacrosse",
#     "JV-F-Lacrosse"
# ])


def update_pulse(consecutive_number_of_requests):
    """
    Update the pulse
    :param consecutive_number_of_requests: the number of requests
    :return: none
    """
    current_time = str(datetime.now())
    ref = db.reference("db-info")
    child_ref = ref.child("pulses")
    child_ref.set({
        "Scrape-Calendar-Pulse": current_time
    })
    ref.child("pulse-numbers").set({
        "Scrape-Calendar-Pulse-Amount (Consecutive)": consecutive_number_of_requests
    })
