from fastapi import FastAPI, HTTPException
from models import Student
from database import students

app = FastAPI(
    title="Student API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Student API"
    }

@app.get("/students")
def get_students():
    return students

@app.get("/students/search")
def search_student(age: int):

    result = []

    for student in students:
        if student["age"] == age:
            result.append(student)

    return result

@app.get("/students/{id}")
def get_student(id: int):

    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

@app.post("/students", status_code=201)
def create_student(student: Student):

    students.append(student.model_dump())

    return student

@app.put("/students/{id}")
def update_student(id: int, student: Student):

    for index, s in enumerate(students):

        if s["id"] == id:
            data = student.model_dump()
            data["id"] = id
            students[index] = data
            return data

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

@app.delete("/students/{id}")
def delete_student(id: int):

    for student in students:

        if student["id"] == id:
            students.remove(student)
            return {
                "message": "Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )