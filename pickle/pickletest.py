students = {
    "Student1":{"Name": "Alice", "Age": 10, "Grade": 4, },
    "Student2":{"Name": "Bob", "Age": 11, "Grade": 5, },
    "Student3":{"Name": "Elena", "Age": 14, "Grade": 8, }
}

print(type(students))

with open("studentInfo.txt", "w") as data:
    data.write(str(students)) #We can only write string objects to tect files
    
with open("studentInfo.txt", "r") as data:
    for student in data:
        print(student)
        
    print(type(student))
    

