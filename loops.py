attempts_left = 3


def passwordCheck1():
    """
    If the user has more than 0 attempts left, they can enter a password. If the password is correct,
    they are welcomed. If the password is incorrect, they are told how many attempts they have left. If
    they have no more attempts left, they are locked out
    """
    while True:
        if attempts_left > 0:
            password = input("Please enter your password ")
            if password == "abc123":
                print("Welcome")
                break
            else:
                print("Incorrect password, attempts remaining: " +
                      str(attempts_left))
                attempts_left = attempts_left - 1
        else:
            print("No more attempts, you are locked out")
            break


def passwordCheck2():
    """
    While the number of attempts left is greater than 0, ask the user to enter their password. If the
    password is correct, print welcome and break out of the loop. If the password is incorrect, print
    the number of attempts remaining and subtract 1 from the number of attempts left. If the number of
    attempts left is 0, print that the user is locked out and break out of the loop.
    """
    while attempts_left > 0:
        password = input("Please enter your password ")
        if password == "abc123":
            print("Welcome")
            break
        else:
            print("Incorrect password, attempts remaining: " + str(attempts_left))
            attempts_left = attempts_left - 1
            if attempts_left == 0:
                print("No more attempts, you are locked out")
                break
