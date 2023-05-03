import pickle

studentNames = ["John", "Jane", "Jack", "Alice", "Bob", "Elena", "Kyle"]

with open("studentFile.pkl", "wb") as f: #opens a text file
    pickle.dump(studentNames, f) #dumps the list into the file or serializes the list into a string
    #wb means that we are writing in binary mode and not text mode
    #wb === write binary mode
    f.close() #to clse the file when done with writing to it.
   
   #=========deserializing================ 
with open("studentFile.pkl", "rb") as f: #opens a text file
    studentNamesLoaded = pickle.load(f) #loads the list from the file or deserializes the string into a list
    print(studentNamesLoaded)
    #rb === read binary is used for deserializing the student names
    
    print(type(studentNamesLoaded))