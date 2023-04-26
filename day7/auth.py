users = {
    "user1":{"email": "user1@example.com", "password": "password1", "verified": True},
     "user2":{"email": "user2@example.com", "password": "password1", "verified": True},
      "user3":{"email": "user3@example.com", "password": "password1", "verified": False},
}

def authenticateUser(func):
    
    def wrapper(*args, **kwargs):
        if kwargs["user"] in users:
            if users[kwargs["user"]]["verified"]:
                return func(*args, **kwargs)
            else:
                print("User not verified")
        else:
            print("User not found")
            
    return wrapper

@authenticateUser
def userAuth(user):
   print("User authenticated")

userAuth(user="user1")