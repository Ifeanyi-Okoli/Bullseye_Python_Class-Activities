fruits = ["Apple", "Orange", "Banana"]

print([x for x in range(20) if x % 2 == 0])  #list comprehension



print({x for x in range(20) if x%2==0}) #set comprehension


even = {y: fruit for y, fruit in enumerate(fruits, start=1)}  #Dictionary comprehension

print(even)

zipped_items = zip(fruits, range(len(fruits)))

print({i:item for i, item in zipped_items})

print(list(zipped_items))


#zip takes two iterables  and put them together into list of tuples

zipped_items = zip(["A", "B", "C"], [0,1,2])


#A generator yields its value.It does not return.

#A generator gives you the item you need at the time. It is more memory efficient than list

#range is an example of generator













































