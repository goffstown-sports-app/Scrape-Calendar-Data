from firebase_admin import db
from datetime import datetime
import platform
import os


def init_field_information_section(list_of_field_names):
    """Inits the field information section of the database

    Arguments:
        list_of_field_names {list} -- list of all the field names
    """
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
            "home-score": 0,
            "away-score": 0,
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


def update_status_database(cleaned_data, current_hour):
    """Updates the field status section of the database

    Arguments:
        cleaned_data {dict} -- data after it has been cleaned
        current_hour {int} -- current hour of the day
    """
    for event in cleaned_data:
        event_hour = event["hour"]
        got_data = 0
        if current_hour == event_hour:
            if "GHS-GYM-FIELD" == event["location"] and event["home"]:
                field_name = "gym"
                got_data += 1
            elif "GHS-FOOTBALL-FIELD" == event["location"] and event["home"]:
                field_name = "football-field"
                got_data += 1
            elif "GHS-SOFTBALL-FIELD" == event["location"] and event["home"]:
                field_name = "softball-field"
                got_data += 1
            ref = db.reference("field-information")
            child_ref = ref.child("field-status/" + field_name)
            current_ref = child_ref.get()
            if got_data != 0:
                try: 
                    if current_ref["home-score"] != type(0) or current_ref["away-score"] != type(0):
                        raise KeyError("Isn't Int")
                    child_ref.set({
                        "sport": event["sport"],
                        "home-score": current_ref["home-score"],
                        "away-score": current_ref["away-score"],
                        "start-time": event["start-time-(normal)"],
                        "away-team-name": event["away_team_name"],
                        "varsity-sport": event["varsity"]
                    })
                except KeyError:
                    child_ref.set({
                        "sport": event["sport"],
                        "home-score": 0,
                        "away-score": 0,
                        "start-time": event["start-time-(normal)"],
                        "away-team-name": event["away_team_name"],
                        "varsity-sport": event["varsity"]
                    })


def init_calendar_section():
    """Initialize the calendar section of the database
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
    """Update the database for the calendar section`

    Arguments:
        list_of_events {list} -- list of all the events from the website
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


def update_pulse(consecutive_number_of_runs, service_name):
    """Updates the pulse for this application

    Arguments:
        consecutive_number_of_runs {int} -- how many times the application has ran in a row
        service_name {str} -- name of the service

    Returns:
        dict -- what the pulse was set as in the database
    """
    current_time = str(datetime.now())
    ref = db.reference("db-info/pulses/" + service_name)
    if "linux" in str(platform.platform()).lower():
        ip_command = str(os.popen("hostname -I").read())
        ip = ip_command.split(" ")[0]
    else:
        ip = ""
    ref_set = {
        "Pulse-Time": current_time,
        "Pulse-Amount-(Consecutive)": consecutive_number_of_runs,
        "Pulse-Node": str(platform.uname().node),
        "Pulse-OS": str(platform.platform()),
        "Pulse-Python-Version": str(platform.python_version()),
        "Pulse-IP": ip
    }
    ref.set(ref_set)
    return ref_set


def set_monitoring_info(email_notifications, pulse_time_diff_secs):
    """Updates the monitoring section for this micro service

    Arguments:
        email_notifications {bool} -- if the user should get email notifications
        pulse_time_diff_secs {int} -- amount of seconds between each pulse (exact)
    """
    ref = db.reference("db-info/monitoring/Scrape-Calendar-Data")
    ref_set = {
        "email-notification": email_notifications,
        "pulse-time-diffs-(secs)": pulse_time_diff_secs + 300,
        "pulse-time-diffs-exact-(secs)": pulse_time_diff_secs
    }
    ref.set(ref_set)
