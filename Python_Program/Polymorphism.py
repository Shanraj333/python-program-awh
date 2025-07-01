class Dog:
    def speak(self):
        print("Woof!")
class Cat:
    def speak(self):
        print("Meow!")
dog=Dog()
cat=Cat()
print("Dog says:",end=" ")
dog.speak()
print("Cat says:",end=" ")
cat.speak()