try:
    f = open("student.txt", "w")
    f.write("Ram\nCarlo\nSam\nManu\nKaran")
    f.close()
    print("Data written successfully.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied. You may not have access to write to this file.")

except Exception as e:
    print("An unexpected error occurred:", e)
