print("This is my first Python Program")  #for printing
statement = "This is my first variabe"  #first variable
print(statement)

"""
This is used for multi-line comment in Python.
"""

#unpacking variables
x, y, z = (1,2,3)

print(z)

#multiple assignment
x = y = z = 3
x, y, x = 3, 3, 3
print(x,y)

#unpacking dsposable variables
x, *y = (1, 2, 3, 4, 5, 6)  # used * when you are not unpacking everything
print(y)