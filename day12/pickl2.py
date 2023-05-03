import pickle

pythonObject = {"name": "Milo", "price": 1200, "quantity": 10}

with open("pythonObject", "rb") as file:
    obj = pickle.load(file)
    print(obj)
    
serializedObj = pickle.dumps(pythonObject)
print(serializedObj)
#withdump, we need to specify a file while with dumps, we do not need to specify a file

pythonno = pickle.loads(serializedObj) #returns a python object from the serialized form
print(pythonno)