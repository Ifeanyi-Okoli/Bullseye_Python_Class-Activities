def f3():
    print("Caled f1")

def f2(f):
    f()

f2(f3) 
# print(f1) 

def f1(func):
    def wrapper(*args, **kwargs): #the args and kwargs allows us to pass as many arguments as possible. The same should be used in the calling of function func(whch is the function f in this case)
        print("Called f1")
        val = func(*args, **kwargs) #this function can be assigned to a variable and returned.
        print("Returned from f1")
        return val
    return wrapper
@f1 #this decorators makes it possible to call function f1 with function f as argument when we call function f
def f(a, b=9):
    print(a, b)

# f1(f)()  #calls the function f1 with function f as argument
# x= f1(f) #this is the function f1 wth function f as argument assigned to variable x. This line can be replaced with decorators @f1

# x() #calling of the function fi with function f as argument
@f1 
def add(x,y):
    return x + y

f("Hi")

print(add(4,5))