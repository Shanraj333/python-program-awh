def calculate_grade(marks):
    if len(marks)!=5:
        print("Invalid!!!")
        return
    total=0
    for i in marks:
        total+=i
    avg=total/len(marks)
    print("Total marks is:", total)
    print("Average is:", avg)
    if avg>=90:
        print("Grade A")
    elif avg>=80:
         print("Grade B")
    elif avg>=70:
         print("Grade C")
    elif avg>=60:
         print("Grade D")
    else:
        print("Fail")


marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
calculate_grade(marks)