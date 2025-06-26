class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def show_details(self):
        print(f", Name: {self.name}, Age: {self.age},ID: {self.student_id}")
class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")
        student = Student(name, age, student_id)
        self.students.append(student)
        print(f"\n Student '{name}' added successfully.\n")
    def display_students(self):
        if not self.students:
            print("\n No students found.\n")
        else:
            print("\n4"
                  " Student Records:")
            for student in self.students:
                student.show_details()
            print()
    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"\nStudent with ID '{student_id}' removed.\n")
                return
        print(f"\n No student found with ID '{student_id}'.\n")
def run():
    manager = StudentManager()
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Remove Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.remove_student()
        elif choice == "4":
            print("\n Exiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

run()
