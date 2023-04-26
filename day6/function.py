print() #for printing
type() #to check type of an object
dir() # to return all attributes of an object
divmod() # returns the whole number and remainder after divisin
sorted() # sorts an iterable without changing the original itareable

name = ""

class Geology:
    def __init__(self) -> None:
        pass
        

def get_user(name:str, age:int, salary:10000, years = 3) -> list:      #two types of arguments - positional and keyword arguments.
    #all positional arguments must come before keyword arguments
    #type can be specified.
    return f"Your name is {name}, age = {age}, salary = {salary}, years={years}"


def get_user(*args, **kwargs) -> list:
    print(args)
    print(kwargs)