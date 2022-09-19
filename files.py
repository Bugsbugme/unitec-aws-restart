# Opening the file data.txt and reading the lines.
data = open("data/data.txt")
fruit = data.readlines()
print(fruit)
data.close()

# Using context manager to open the file data.txt and reading the lines.
with open("data/data.txt") as data:
    fruit = data.readlines()
    print(fruit)
