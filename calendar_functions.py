import utility_functions as UF
from requests import Request, Session
import json


def get_events_for_day(day, month, year):
    """
    Get event information for the events of the day
    :param day: day to query (int)
    :param month: month to query (int)
    :param year: year to query (int)
    :return: events (list)
    """
    # Type checking:
    UF.check_type(day, "int")
    UF.check_type(month, "int")
    UF.check_type(year, "int")

    # Querying information:
    data = 'CalMonth={m}&CalYear={y}&CalDay={d}'.format(m=month, d=day, y=year)
    url = 'https://goffstownathletics.com/main/calendarDayAjax'
    headers = {
        'origin': 'https://goffstownathletics.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': 'JSESSIONID=A437B190923E2C2C1845AF70D5346A7D.Main; erd=6B749E34B06E77B4303C2CF244678ECD; CALVIEW=month; CALDATE={m}/{d}/{y}; AWSALB=e/KIOyE3YhuKL9TvYnaun6DDc9LkzOc+G7+DLvkNdZ9KMu70lUN9dcxt0g5OwJoBLTJgglZ3Tk91OhPU7KZXRz9GUslWJ60RiMNq+6YgwEEwnvdQIGNPVfNKisoh'.format(
            m=month, d=day, y=year),
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'cache-control': 'no-cache',
        'authority': 'goffstownathletics.com',
        'referer': 'https://goffstownathletics.com/main/calendar/',
    }
    s = Session()
    req = Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_request(req)
    resp = s.send(prepped)
    respJson = json.loads(resp.content)
    if len(respJson) == 0:
        return None
    else:
        return respJson

# Testing:
# print(get_events_for_day(6, 6, 2019))


def cleaning_response(json_data, day, month, year):
    """
    Will clean the json response from the website.
    :param json_data: json response from the calendarAjax file
    :param day: day that was queried (int)
    :param month: month that was queried (int)
    :param year: year that was queried (int)
    :return: cleaned data (list)
    """
    # Type Checking:
    if json_data == None:
        return None
    else:
        UF.check_type(json_data, "list")
        UF.check_type(day, "int")
        UF.check_type(month, "int")
        UF.check_type(year, "int")

        #  Cleaning Data:
        if len(json_data) == 0:
            return None
        else:
            event_amount = 0
            clean_events = []
            for event in json_data:
                event_amount += 1
                if event["isCancelled"] == 0:
                    cancelled = False
                elif event["isCancelled"] == 1:
                    cancelled = True
                if "boys" in event["theTitle"].lower():
                    gender = "m"
                elif "girls" in event["theTitle"].lower():
                    gender = "g"
                if "junior" in event["theTitle"].lower() and "varsity" in event["theTitle"]:
                    varsity = False
                elif "varsity" in event["theTitle"].lower():
                    varsity = True
                if "middle" in event["theTitle"].lower():
                    ghs_sport = False
                elif "middle" not in event["theTitle"].lower():
                    ghs_sport = True
                if event["homeOrAway"] == 1:
                    home = True
                elif event["homeOrAway"] == 0:
                    home = False
                location = event["thePlace"].strip("@").strip()
                thedate_elements = event["thedate"].split("vs")
                normal_time = thedate_elements[0].strip("(H)").strip("(A)").strip()
                datetime_form = UF.normal_time_to_datetime(normal_time, day, month, year)
                hour = datetime_form.hour
                minute = datetime_form.minute
                away_team_name = thedate_elements[1].strip()
                thetitle_elements = event["theTitle"].split(" ")
                last_two_items = thetitle_elements[-2:len(thetitle_elements)]
                if "varsity" == last_two_items[0].lower():
                    sport_name = last_two_items[1]
                else:
                    sport_name = " ".join(last_two_items)
                event_dict = {
                    "gender": gender,
                    "varsity": varsity,
                    "ghs_sport": ghs_sport,
                    "home": home,
                    "event_location": location,
                    "start-time-(normal)": normal_time,
                    "stat-time-(datetime)": datetime_form,
                    "hour": hour,  # Military time
                    "minute": minute,  # Military time
                    "away_team_name": away_team_name,
                    "sport": sport_name,
                }
                clean_events.append(event_dict)
            return clean_events


# Testing:
# print(cleaning_response(get_events_for_day(3, 6, 2019), 3, 6, 2019))
