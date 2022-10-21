def add(a, b):
    # return a + b
    try:
        result = a + b
    except TypeError:
        result = 0

    return result
