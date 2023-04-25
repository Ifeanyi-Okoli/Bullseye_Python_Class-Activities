#Reverse the string, make the middle character the first and the first, the middle.
mystr= "djfifrjdnkaodeueygforoee"
mid = len(mystr)//2
newstr = mystr[::-1]
print(newstr[mid] + newstr[1:mid] + newstr[0] + newstr[mid+1:])

#------------------task 2-------------------
import random
myname = "Ifeanyi Okoli".split(" ")
name = random.choice(list("Ifeanyi-Okoli"))
age = [5, 2, 1, 7, 8]


for i in age:
    childs_name = ""
    while i >0:
        
        childs_name += random.choice(list("IfeanyiOkoli"))
        i -= 1
    print(childs_name + " " + myname[1])

#-------------------correction----------------

def childrenNames(nameOfFather:str, childrenAge:list) -> list:
    childrenNames = []

    first_name, last_name = nameOfFather.split(" ")

    for age in childrenAge:

        kidName=""

        if age > len(first_name):
            first_name = first_name + first_name[:len(first_name)//2]

        for _ in range(age):
            kidName += random.choice(first_name)

        kidFullName = kidName.capitalize() + " " + last_name
        childrenNames.append(kidFullName)
    return childrenNames


print(childrenNames("Ifeanyi Okoli", [4, 5, 7, 2]))






















