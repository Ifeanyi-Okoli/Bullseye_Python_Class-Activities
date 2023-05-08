import json

person = {
    "name": "Umaru Jamiu",
    "Age": 20,
    "status": "single",
    "children": ["Aisha", "Amina", "Abdul"],
    "Salary": 1000000
}

#json is used to make files readable and exchangeable across programming ends and languages

jsonPerson = json.dumps(person)

print(type(jsonPerson))
print(type(person))


with open("person.json", "a") as file:
    json.dump(jsonPerson, file)
    

# use picckle for transmitting between sockets but same language. Binary File is a serialized file that is saved in a computer friedly format.

#dumps is used to serialized python objects into JSON formated string
#dump is used to serialized python objects into JSON formated string and save it in a file