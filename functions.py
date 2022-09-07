# def greeting(name):
#     """
#     The function takes in a name and returns a greeting if the name is a string, otherwise it returns an
#     error message

#     :param name: The name of the person you want to greet
#     :return: the print statement.
#     """
#     if isinstance(name, str):
#         return print(f"Hello {name}")
#     else:
#         return "Error: Integers not allowed"


# greeting("Gracie")


# def greeting2(f_name, l_name):
#     """
#     If the first and last name are strings, print a greeting. Otherwise, return an error message

#     :param f_name: first name
#     :param l_name: last name
#     :return: the print statement.
#     """
#     if isinstance(f_name, str) & isinstance(l_name, str):
#         return print(f"Hello {f_name} {l_name}")
#     else:
#         return "Error: Integers not allowed"


# greeting2("Gracie", "Bryan")


# def greeting3(*names):
#     """
#     The function takes in a variable number of arguments and prints them out
#     """
#     print(f"Hello {names}")


# greeting3("Gracie", "Nick", "Ben")


# def add_numbers(*nums):
#     """
#     It takes in any number of arguments and adds them all together
#     """
#     total = 0
#     for num in nums:
#         total = total + num
#         print(total)


# add_numbers(1, 8, 5, 3, 6)


# def show_props(**car):
#     """
#     It takes a dictionary as an argument and prints out the key-value pairs
#     """
#     for i in car.items():
#         print(i)


# show_props(make="Toyota", model="Corolla", year=2008, colour="Yellow")


# def function_with_default(name="Gracie"):
#     """
#     The function takes in a name and prints it out. If no name is given, it prints out "Gracie"

#     :param name: This is a positional parameter, defaults to Gracie (optional)
#     """
#     print(name)


# function_with_default()


# def dictionary_maker(**kwargs):
#     """
#     It takes any number of keyword arguments and returns a dictionary with those keys and values
#     :return: A dictionary
#     """
#     return kwargs


# car = dictionary_maker(make="Toyota", model="Corolla", year=2008, colour="Yellow")


def good_morning():
    """
    It returns the string "Good morning"
    :return: "Good morning"
    """
    return "Good morning"


def good_afternoon():
    """
    It returns the string "Good afternoon"
    :return: The string "Good afternoon"
    """
    return "Good afternoon"


def door_man(time):
    """
    If the time is sunrise, return good morning, if the time is sunset, return good afternoon, otherwise
    return unknown time.

    :param time: a string
    :return: The function good_morning() is being returned.
    """
    if time == "sunrise":
        return good_morning()
    elif time == "sunset":
        return good_afternoon()
    else:
        return "unknown time"


# print(door_man("sunset"))


def door_man2(fn):
    """
    It takes a function as an argument, runs it, and prints the result

    :param fn: The function that is being decorated
    """
    print("Running function...")
    print(fn())
    print("Finished running function.")


door_man2(good_morning)
