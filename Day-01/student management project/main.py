from model import Student

students: list[Student] = []


def add_student():
    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    student = Student(student_id, name, age)
    students.append(student)

    print("Student Added Successfully")


def view_students():
    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:
        print(student)


def search_student():
    student_id = int(input("Enter ID: "))

    for student in students:
        if student.id == student_id:
            print(student)
            return

    print("Student Not Found")


def update_student():
    student_id = int(input("Enter ID: "))

    for student in students:
        if student.id == student_id:
            student.age = int(input("Enter New Age: "))
            print("Updated Successfully")
            return

    print("Student Not Found")


def delete_student():
    student_id = int(input("Enter ID: "))

    for student in students:
        if student.id == student_id:
            students.remove(student)
            print("Deleted Successfully")
            return

    print("Student Not Found")


while True:

    print("\n===== Student Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")