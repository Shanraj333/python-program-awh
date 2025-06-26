i = int(input("Enter a number between 1 and 50:"))
if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz")
elif i % 3 == 0:
       print("Fizz")
elif i % 5 == 0:
       print("Buzz")
else:
       print(i)
