class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("ID:",self.id)
student=Student("Rahul",23,"s12")
student.show_details()
