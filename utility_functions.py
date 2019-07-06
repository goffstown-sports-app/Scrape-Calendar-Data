from datetime import datetime


def check_type(item, expected_type):
    """
    Checks a object to make sure that it is a certain type
    :param item: any type
    :param expected_type: string (ex:"str")
    :return: type
    """
    item_type = str(type(item))
    if "str" in expected_type.lower() and item_type == "<class 'str'>":
        pass
    elif "int" in expected_type.lower() and item_type == "<class 'int'>":
        pass
    elif "bool" in expected_type.lower() and item_type == "<class 'bool'>":
        pass
    elif "float" in expected_type.lower() and item_type == "<class 'float'>":
        pass
    elif "tuple" in expected_type.lower() and item_type == "<class 'tuple'>":
        pass
    elif "list" in expected_type.lower() and item_type == "<class 'list'>":
        pass
    elif "dict" in expected_type.lower() and item_type == "<class 'dict'>":
        pass
    elif "datetime" in expected_type.lower() and item_type == "<class 'datetime.datetime'>":
        pass
    elif "none" in expected_type.lower() and item_type == "<class 'NoneType'>":
        pass
    else:
        raise Exception("{a} isn't a {b}".format(a=object, b=expected_type))
    return item_type


# Testing
# check_type(8, "int")
# check_type(1.1, "float")
# check_type([], "list")
# check_type({}, "dict")
# check_type((), "tuple")
# check_type(True, "bool")
# check_type("testing testing", "str")


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