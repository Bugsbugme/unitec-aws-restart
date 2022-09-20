# Working with modules
from data import hello_module

# This is calling the graffiti function in the hello_module.py file and printing the result.
result = hello_module.graffiti()
print(result)
print("Attempting to clean...")

# This is a try/except/finally block. The try block is the code that is being tested. The except block
# is the code that is executed if the try block fails. The finally block is the code that is executed
# regardless of whether the try block succeeds or fails.
try:
    hello_module.clean()
except hello_module.MyError:
    print("Error cleaning my camera, T-1000's have been dispatched.")
finally:
    print("This always occurs.")
