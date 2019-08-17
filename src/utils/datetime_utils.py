from datetime import datetime


def normal_time_to_datetime(normal_time, day, month, year):
    """Converts normal time format to a datetime object

    Arguments:
        normal_time {string} -- normal time
        day {int} -- normal time day
        month {int} -- normal time month
        year {int} -- normal time year

    Returns:
        datetime -- iso datetime version of the normal time
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
