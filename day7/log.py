import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write("Function: {} called at: {} with arguments: {} and keyword arguments: {} \r ".format(func.__name__, datetime.datetime.now(), args, kwargs))
        val = func(*args, **kwargs)
        return val
    return wrapper

@log
def run(a, b, c=9):
    print(a+b+c)
    
run(1,3, c=9)









