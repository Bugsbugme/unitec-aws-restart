def graffiti():
    """
    It prints "Gracie was here" and returns the number 123.
    :return: 123
    """
    print("Gracie was here")
    return 123


def clean():
    """
    This function raises an error
    """
    raise MyError


# It's a class that inherits from the Exception class
class MyError(Exception):
    pass
