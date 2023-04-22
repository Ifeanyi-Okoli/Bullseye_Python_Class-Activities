#tuples are immutable and are created using bracket
month = (1,2,3,4,5,6,7,8,9,10,11,12)
#In tuples you cannot change contents, but you can change contents of the content of the tuple.add()
months = ([1, 3, 4],)
months[0][2] = 6
print(months)
#----------set----------------------
#we define a set using curly braces. To define an empty set, we use set().add()
# set does not permit repitition. We use set when we dont want names of people appearing twice.
man = set()
man = {"Ifeanyi", "Okoli", "Ifeanyi", "Okoli"}
print(man)


class1 = {"Newman", "Niyi", "Niyi", }
class2 = {"John", "Noman", "Niyi"}

print(class1.difference(class2))  #prints the difference between the two sets

print(class1.union(class2))

from string import ascii_letters, punctuation, ascii_uppercase, ascii_lowercase, digits

letters_lower = set(ascii_lowercase)
letters = set(ascii_letters)
print(letters.difference(letters_lower))


A = set("ABab12@45")
B = set("Ab1570&&")
print(A.symmetric_difference(B))  #opposite of intersection. It gives what is unique to A and B

A.add("9")
B.discard("A") #discard is equivalentto remove
print(A)

#--------List-----------------

# A list is a collection of items
carts = list()
carts = []
carts = list(set())

#lists hold items in order
carts = [1,2,3,4,5]
#you can have other data types in the list
# you can have nested lists. You can have a list of lists
carts = [[1,2,3,4,5], [6,7,8,9,10]]

#we use append to add new items to alist
carts.append([])
print(carts)
i = carts.index(5)
print(i)
#pop returns removed items, but remove does not return removed items
#to pop, you use the idex, but when popping, use the index
carts.insert(i, "orange")
removed = carts.pop(i)

cart = ["banana", "guava"]
carts.extends(cart)
cart3 = carts + cart
print(cart3 * 3)


#












































































