# [11:45 AM] Maruche Nwokocha




# Create a function to calculate tax from salary of a worker. specify the name, department, and position of the worker as position argument. Salary as keyword arguments.


# [11:45 AM] Maruche Nwokocha




# Also specify datatypes for the arguments and the returned value
name = "Ifeanyi Okoli"
dept = "Computer"
post = "Lecturer"


def staffTax(name:str, dept:str, post:str, salary=100000, tax=0.1) -> str:
    
    return f"{name} from {dept} department, {post} position, salary is {salary}, tax is {tax*salary}"

print(staffTax(name, dept, post))

#keyword arguments are accessed as dictionary
#positional arguments are accessed as string arguments
#3 ways to format a string - f string, format and the % mthod






































