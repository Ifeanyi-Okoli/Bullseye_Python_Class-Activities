#Exceptions arevraised when something is wrong
try:
    print(10/0)  #zero division error
except:
    print("Hello")

value = [1,2,3,4,5,6,7,8,9,00,2]
for value in values:
    try:
        print(10/value) #zero division error
    except ValueError as e:
        print(str(e))
    except ZeroDivisionError as e:
        print(str(e))
        