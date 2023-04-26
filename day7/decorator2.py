#complex decorator, where the decorator has arguments
#school pays bursary only to state indigenes and there are students that are not indigenes. Year 1 gets noothing, year 2 bursary is different from year 3 


# def payBursary(student):
#     if student["state"] == "Lagos":
#         return student["bursary"] + 10000
#     else:
#         return student["bursary"]

from decorator3 import isIndigine
@isIndigine(state="None", years=2, amount=50000)
def payBursary(student):
    if student.get("isPaid"):
        return student
    return student


students = [
    {"name": "Ayo", "state": "Lagos", "years": 2, "bursary": 10000, "dept": "Computer Science", "cgpa": 4.5},
    {"name": "AYoide Daramola", "state": "Ogun", "years": 2, "bursary": 10000, "dept": "Computer Science", "cgpa": 4.5},
    {"name": "Nichola Cole", "state": "Imo", "years": 3, "bursary": 30000, "dept": "Computer Science", "cgpa": 4.5},
    {"name": "Osaro Ogbemudia", "state": "Osun", "years": 4, "bursary": 50000, "dept": "Computer Science", "cgpa": 4.5},
    {"name": "James Dayo", "state": "Delta", "years": 2, "bursary": 40000, "dept": "Computer Science", "cgpa": 4.5},
]

for student in students:
    paidStudent = payBursary(student)
    print(paidStudent)
    
    

# def isIndigine(state, year, amount):
#     def inner(func):
#         def wrapper(student):
#             if state is None:
#                 student.update({"paid": amount, "isPaid": True})
#             elif student["level"] == year:
#                     student.update({"paid":amount, "isPaid":True})
                
#             else:
#                 return student["bursary"]
#         return wrapper
#     return inner