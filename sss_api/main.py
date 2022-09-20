from fastapi import FastAPI

app = FastAPI()

# Data
#   student [list]
#     student name
#     student id

student_list = [
    "Marcelle",
    "Bevan",
    "Anuj",
    "Kawana",
    "Ryan",
    "Kura",
    "Luke",
    "Kate",
    "Prerana",
    "Stacey",
    "Xavier",
    "Gracie",
    "Quentin",
    "Ben",
    "Raemon",
    "Dave",
    "Benke",
    "Jayam",
    "Will",
    "James",
]

# Functions
#   Select random student
def select_random_student():
    # Select student
    pass


#   List of current students
@app.get("/students")
def current_students():
    return student_list


#   List of students who have shared
def shared_students():
    pass
