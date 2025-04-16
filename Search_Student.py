import json
import os

def search_student():
    try:
        path = "students.json"

        if not os.path.exists(path):
            print("student data file not found. No student records available.")
            return

        with open(path, "r") as file:
            students = json.load(file)

        if not students:
            print("student data is empty. No student records found.")
            return

        student_input = input("enter student id or contact to search: ")

        for student in students:
            if student["id"] == student_input or student["contact"] == student_input:
                print("\nstudent found:")
                for key, value in student.items():
                    print(f"{key}: {value}")
                return

        print("student not found.")
    except Exception as e:
        print(f"error during search: {e}")
