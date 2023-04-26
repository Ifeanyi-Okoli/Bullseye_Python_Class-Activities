# A decorator must be defined before it can be used.
#Inner function of a decorator is called a wrapper
#Decorator is used to extend a function


def isSubscribed(func):
    subscribers = ["America", "Nina", "Ayo", "Tayo"]
    def wrapper(user):
        if user["name"] in subscribers:
            user.update({"isSubscribed": True})
            return func(user)

    return wrapper

def showMovie():
    print("Showing Movie")
    
@isSubscribed  #a decorator
def viewMovie(user):
    try:
        if user["isSubscribed"]:
            lambda x: print("Showing Movie")
    except:
        print("Please subscribe to watch the movie")



# @isSubscribed  #a decorator
# def removeMovie(user):
#     try:
#         if user["isSubscribed"]:
#             remove()
#     except:
#         print("Please subscribe to watch the movie")

        
user = {"name": "Ayo"}

viewMovie(user)
# removeMovie(user)
#decorators can be reused several times