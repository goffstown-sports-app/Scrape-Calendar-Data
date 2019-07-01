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
    firebase_admin.initialize_app(cred, {"databaseURL": "https://ghs-app-5a0ba.firebaseio.com"})
    ref = db.refernce("field_information")
    general_information_path = 