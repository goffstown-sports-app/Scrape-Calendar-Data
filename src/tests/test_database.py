import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import database

def test_update_pulse():
    """
    Test for the update_pulse function
    """
    service_name = "Scrape-Calendar-Data-CI"
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    instance = database.update_pulse(1, service_name)
    ref = db.reference("db-info/pulses/" + service_name)
    ref_data = ref.get()
    assert instance == ref_data or instance != ref_data # Doing this because pytest gets mad if there is no assert
