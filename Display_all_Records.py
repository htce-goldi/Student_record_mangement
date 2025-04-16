import json
import os
def display_students():
      try:
           file_path = "students.json"
  
           if os.path.exists(file_path):
            with open(file_path, "r") as file:
                students = json.load(file)
           else:
            students = []
           if not students:
            print("no student records found.")
            return

           print("\nlist of registered students:")
           for student in students:
            print()
            for key, value in student.items():
                print(f"{key}: {value}")
                
            print()
      except Exception as e:
            print(f"error: {e}")
