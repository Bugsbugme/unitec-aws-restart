# Screen Share Randomizer
# Get a list of students
# Choose a student from that list and then remove them

from os import system
from pathlib import Path
from random import choice


def initializeStudentList(savPath, initPath):
    """
    If the file at savPath exists, read it into studentsList, if it's empty, write the contents of
    initPath to it, then read it into studentsList. If the file at savPath doesn't exist, create it,
    write the contents of initPath to it, then read it into studentsList

    :param savPath: The path to the file that will be saved
    :param initPath: The path to the file that contains the initial list of students
    :return: A list of students
    """
    studentsList = []
    if savPath.exists():
        studentsList = open(savPath).readlines()
        if not (studentsList):
            print("Save file empty, rebuilding...\n")
            open(savPath, "w").writelines(open(initPath).readlines())
            studentsList = open(savPath).readlines()
    else:
        print("Save file does not exist, building new one...\n")
        open(savPath, "x").writelines(open(initPath).readlines())
        studentsList = open(savPath).readlines()
    return studentsList


# end def


system("cls")

initPath = Path("data/students_init.txt")
savPath = Path("data/students_sav.txt")
studentsList = initializeStudentList(savPath, initPath)

student = choice(studentsList)
print(f"{student.strip()} has been chosen for screen sharing\n")

studentsList.remove(student)
print(f"{len(studentsList)} Student(s) remaining:")
for student in studentsList:
    print(student.strip())
open(savPath, "w").writelines(studentsList)
