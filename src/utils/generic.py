def check_type(item, expected_type):
    """Check the datatype of an object
    
    Arguments:
        item {object} -- the object to check
        expected_type {string} -- expected type of object 
    
    Raises:
        TypeError: That the type isn't as expected
    
    Returns:
        string -- datatime of the item gotten with type()
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
        raise TypeError("{a} isn't a {b}".format(a=object, b=expected_type))
    return item_type


# Testing
# check_type(8, "int")
# check_type(1.1, "float")
# check_type([], "list")
# check_type({}, "dict")
# check_type((), "tuple")
# check_type(True, "bool")
# check_type("testing testing", "str")
