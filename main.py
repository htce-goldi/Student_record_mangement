import Student_Registration
import Display_all_Records 
import Search_Student

def menu():
    while True:
        print("\n student record management ")
        print()
        
        print("press 1 for register Student")
        print("press 2 for display all students")
        print("press 3 for search student")
        print("press 0 for exit")
        option = input("please select any option: ")

        if option == "1":
            Student_Registration.register_student()
        elif option == "2":
            Display_all_Records.display_students()
        elif option == "3":
            Search_Student.search_student()
        elif option == "0":
            print("exiting program!")
            break
        else:
            print("invalid option. please select the correct option")
            
menu()

