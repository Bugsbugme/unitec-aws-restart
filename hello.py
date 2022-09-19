from data import hello_module

result = hello_module.graffiti()
print(result)
print("Attempting to clean...")

try:
    hello_module.clean()
except hello_module.MyError:
    print("Error cleaning my camera, T-1000's have been dispatched.")
finally:
    print("This always occurs.")
