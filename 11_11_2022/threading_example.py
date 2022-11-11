import threading
import time


def hello(name):
    print(f"{name} is going to sleep...")
    time.sleep(5)
    print(f"{name} just woke up")


hello("Nemo")
hello("Marlin")
hello("Dori")

# Creating a thread object to run the `hello` function.
t1 = threading.Thread(target=hello, args=["Manny"])
t2 = threading.Thread(target=hello, args=["Sid"])
t3 = threading.Thread(target=hello, args=["Diego"])

# Calling the `run` method of the `t1` object.
t1.start()
t2.start()
t3.start()
