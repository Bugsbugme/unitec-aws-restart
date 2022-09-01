# Screen Share Randomizer
# Get a list of students
# Choose a student from that list and then remove them

import random

# Opening the file students_tmp.txt and reading the lines into a list called students.
read_students = open("data/students_tmp.txt")
students = read_students.readlines()

# If the students list is empty, then it will open the students_init.txt file and read the lines into
# the students list.
if students.__len__() == 0:
    students_init = open("data/students_init.txt")
    students = students_init.readlines()
    students_init.close()

# Choosing a random student from the list and printing it out.
student = random.choice(students)
print(student.strip() + " has been chosen for screen sharing")

# Removing the student from the list and update students.tmp
students.remove(student)
students_tmp = open("data/students_tmp.txt", "w")
students_tmp.writelines(students)
students_tmp.close()

# Printing the contents of the file students_tmp.txt.
students_tmp = open("data/students_tmp.txt")
print(students_tmp.readlines())
students_tmp.close()
