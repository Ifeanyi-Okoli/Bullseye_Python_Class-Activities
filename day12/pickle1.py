import pickle
#persistence is the practice of saving data in a database
pythonObject = {"name": "Milo", "price": 1200, "quantity": 10}

#pickle has 2 major methods - for saving and for serializing

#dump serializes and saves in the file
#dumps serializes, doesn't save and returns a string
#pickle is better because unlike txt files, it is not possibble to alter the content of serialized objects.
with open("pythonObject", "ab") as file:
    pickle.dump(pythonObject, file)