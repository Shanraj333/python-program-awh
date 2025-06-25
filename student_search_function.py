def add_student():
    try:
        names = input("Enter student name(s), separated by commas: ").strip()
        name_list = [name.strip().capitalize() for name in names.split(",") if name.strip()]
        with open("students.txt", "a") as f:
            for name in name_list:
                f.write(name + "\n")
        print("Student(s) added successfully:")
        for name in name_list:
            print(name)
    except Exception as e:
        print("Error:", e)
def view_students():
    try:
        with open("students.txt", "r") as f:
            students = f.readlines()
            if not students:
                print("No students found.")
            else:
                print("\n--- Student List ---")
                for student in students:
                    print(student.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)
def search_student():
    try:
        search_name = input("Enter name to search: ").strip().lower()
        flag = 0
        with open("students.txt", "r") as f:
            for line in f:
                if search_name == line.strip().lower():
                    flag = 1
                    break
        if flag==1:
            print(f"'{search_name}' found in the list.")
        else:
            print(f"'{search_name}' not found.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)
def count_students():
    try:
        with open("students.txt", "r") as f:
            count = len(f.readlines())
        print(f"Total number of students: {count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)
def menu():
    while True:
        print("\n--- Student Management ---")
        print("1. View student list")
        print("2. Add a student")
        print("3. Search for a student")
        print("4. Count total students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            count_students()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
menu()







