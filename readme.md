# Gracie's MCAWS - AWS re/Start practice files 💻

![profile_picture](https://media-exp1.licdn.com/dms/image/D4D35AQHyYaRsPHQ_Yw/profile-framedphoto-shrink_400_400/0/1656900440723?e=1663560000&v=beta&t=YSZEtAeIxeWLQ1SBphZfwA69b6WG--QaXQtdQKIU6ZI)

- [Gracie on GitHub](https://github.com/Bugsbugme)
- [Gracie on LinkdIn](https://www.linkedin.com/in/gracie-bryan)

## python()

- [if()](/age_check.py)

```python
# Asking the user for their age and then printing out a message depending on whether they are old
# enough to buy alcohol.
age = int(input("What is your age? "))
if age >= 18:
    print("You are old enough to buy this alcohol")
else:
    print("Sorry, come back when you're older")

```

- [functions](/function.py)

```python
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
```

- [while loops](/loops.py)

```python
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
```
