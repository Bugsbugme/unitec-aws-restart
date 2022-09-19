def graffiti():
    print("Gracie was here")
    return 123


def clean():
    raise MyError


class MyError(Exception):
    pass
