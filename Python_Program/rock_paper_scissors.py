import random
print("Welcome to the game")
a=int(input("Enter your choice:(rock:1,paper:2,scissors:3):"))
if a>3:
    print("Your choice is invalid")
    print("Please enter a valid choice")
else:
    b=random.randint(1,3)
    print("Computer's choice is ",b)
    if a==b:
        print("it's a draw")
    elif a==1 and b==2:
        print("computer wins")
    elif a==1 and b==3:
        print("You wins")
    elif a==2 and b==1:
        print("You wins")
    else:
        print("computer wins")