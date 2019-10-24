import requests

from utils import datetime_utils


def get_events_for_day(day, month, year):
    """Query's the events from the website

    Arguments:
        day {int} -- day to query
        month {int} -- month to query
        year {int} -- year to query

    Returns:
        dict -- queryied result
    """
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
    session = requests.Session()
    req = requests.Request('GET', url, data=data, headers=headers)
    prepped = session.prepare_request(req)
    resp = session.send(prepped).json()
    session.close()
    if len(resp) == 0:
        return None
    if resp == {'message': 'Flag On the Play!', 'detail': 'Do not worry, we are now checking this.'}:
        return None
    return resp

# Testing:
# print(get_events_for_day(6, 6, 2019))


def cleaning_response(json_data, day, month, year):
    """Cleaning the Queried Response

    Arguments:
        json_data {dict} -- queried response from the website
        day {int} -- day that was queried
        month {int} -- month that was queried
        year {int} -- year that was queried

    Returns:
        dict -- clean version of the queried response
    """
    #  Cleaning Data:
    if json_data is None:
        return None
    else:
        event_amount = 0
        clean_events = []
        for event in json_data:
            if "middle" in event["theTitle"].lower() and "school" in event["theTitle"].lower():
                pass
            elif "practice" in event["eventType"].lower() or "scrimmage" in event["eventType"].lower():
                pass
            elif "spirit" in event["theTitle"].lower():
                pass 
            else:
                event_amount += 1
                if event["isCancelled"] == 0:
                    cancelled = False
                elif event["isCancelled"] == 1:
                    cancelled = True
                if "boys" in event["theTitle"].lower():
                    gender = "m"
                elif "girls" in event["theTitle"].lower():
                    gender = "g"
                if "junior" in event["theTitle"].lower() and "varsity" in event["theTitle"].lower():
                    varsity = False
                elif "varsity" in event["theTitle"].lower():
                    varsity = True
                else:
                    varsity = False
                if "middle" in event["theTitle"].lower():
                    ghs_sport = False
                elif "middle" not in event["theTitle"].lower():
                    ghs_sport = True
                if event["homeOrAway"] == 1:
                    home = True
                elif event["homeOrAway"] == 0:
                    home = False
                location = event["thePlace"].strip("@").strip()
                thedate_elements = event["thedate"].strip(
                    "(H)").strip("(A)").strip().split(" ")
                normal_time = thedate_elements[0]
                datetime_form = datetime_utils.normal_time_to_datetime(
                    normal_time, day, month, year)
                hour = datetime_form.hour
                minute = datetime_form.minute
                if "vs" in event["thedate"]:
                    away_team_name = " ".join(event["thedate"].split(" ")[3:])
                else:
                    away_team_name = " ".join(event["thedate"].split(" ")[2:])
                thetitle_elements = event["theTitle"].split(" ")
                last_two_items = thetitle_elements[-2:]
                if "varsity" == last_two_items[0].lower():
                    sport_name = last_two_items[1]
                else:
                    sport_name = " ".join(last_two_items)
                if varsity and home:
                    if "soccer" in sport_name.lower():
                        location = "GHS-FOOTBALL-FIELD"
                    elif "football" in sport_name.lower():
                        location = "GHS-FOOTBALL-FIELD"
                    elif "lacrosse" in sport_name.lower():
                        location = "GHS-FOOTBALL-FIELD"
                    elif "softball" in sport_name.lower():
                        location = "GHS-SOFTBALL-FIELD"
                    elif "volley" in sport_name.lower():
                        location = "GHS-GYM-FIELD"
                    elif "basketball" in sport_name.lower():
                        location = "GHS-GYM-FIELD"
                    elif "field" in sport_name.lower() and "hockey" in sport_name.lower():
                        location = "GHS-FOOTBALL-FIELD"
                event_dict = {
                    "gender": gender,
                    "varsity": varsity,
                    "ghs_sport": ghs_sport,
                    "home": home,
                    "location": location,
                    "start-time-(normal)": normal_time,
                    "stat-time-(datetime)": datetime_form,
                    "hour": hour,  # Military time
                    "minute": minute,  # Military time
                    "away_team_name": away_team_name,
                    "sport": sport_name,
                    "cancelled": cancelled
                }
                clean_events.append(event_dict)
        if len(clean_events) == 0:
            return None
        return clean_events


# Testing:
# print(cleaning_response(get_events_for_day(3, 6, 2019), 3, 6, 2019))
