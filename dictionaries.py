my_dictionary = {
    "Gracie": 1,
    "Stacey": 2,
    "Kris": 3,
}
for key in my_dictionary.keys():
    print(key)
for value in my_dictionary.values():
    print(value)
for item in my_dictionary.items():
    print(item)
for key, value in my_dictionary.items():
    my_dictionary[key] = value + 1
