def function_countlines():
     f=open("student.txt", "r")
     lines=f.readlines()
     print(f"The number of lines is:{len(lines)}")
function_countlines()