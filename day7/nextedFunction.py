# Closure is the concept in which the inner function has access to the scope of the outer function
def outer(x):
    
    def inner(y):
        print(x, y)
        return x * y
    return inner

inner = outer(10)
print(inner(7))

#