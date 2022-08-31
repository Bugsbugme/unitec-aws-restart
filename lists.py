list1 = ["hello", "hello", 1, 24, 5]
list5 = [1, 2, 3, 4, 5]


print(list1.index("hello"))
# list1.append("aws")
# list1.insert(1, "Gracie")
# list1.remove(5) #removes specific value
# list1.pop(3) #removes specific index
# list1.reverse()
list2 = list1.copy()

list1.append("aws")
list2.insert(1, "Gracie")
print(list1.count("hello"))
# print(list1.reverse())

var = list2.clear()

list1.extend([1, 2, 3])
# list1.sort()

# print(list1.__getitem__(3))
hello = list1.__contains__("hello")
thing = list1.__getitem__(7)
list1.__delitem__(2)
# list5.__format__()
