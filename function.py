def greeting(name):
    """
    If the input is a string, return "Hello " + name, otherwise return "Error: Integers not allowed"

    :param name: The name of the person you want to greet
    :return: "Hello " + name
    """
    if isinstance(name, str):
        return "Hello " + name
    else:
        return "Error: Integers not allowed"


print(greeting())
