import json
import os
def register_student():
    
    try:
        file_path = "students.json"

       
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                students = json.load(file)
        else:
         students = []

        new_student = {
            "id": input("enter student's id:- "),
            "name": input("enter student's name:- "),
            "email": input("enter student's email:- "),
            "address": input("enter student's address:- "),
            "contact": input("enter student's contact number:- "),
            "qualification": input("enter student's qualification:- ") 
            
        }
        for student in students:
            if student["id"] == new_student["id"]:
                print("student with this id already exists.")
                return

        students.append(new_student)
        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)

        print("student registered successfully!")

    except Exception as e:
        print(f"error during registration: {e}")
