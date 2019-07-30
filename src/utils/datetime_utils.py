from datetime import datetime


def normal_time_to_datetime(normal_time, day, month, year):
    """
    Turns normal time and returns a normal time
    :param normal_time: normal time (str, ex: 4:30PM)
    :param day: the day (int)
    :param month: the month (int)
    :param year: the year (int)
    :return: ISO time (str)
    """
    if "am" in normal_time.lower():
        time_elements_strs = normal_time.strip("AM").split(":")
    else:
        time_elements_strs = normal_time.strip("PM").split(":")
    hour = int(time_elements_strs[0])
    minute = int(time_elements_strs[1])
    if "pm" in normal_time.lower():
        hour += 12
    iso_version = datetime(year, month, day, hour, minute)
    return iso_version


# Testing:
# print(normal_time_to_datetime("5:23PM", 4, 6 ,2004))
