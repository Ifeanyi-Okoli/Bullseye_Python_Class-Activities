import random
import math
#range isa agenerator
# print (range(100))
# print (list(range(100)))
# int() is equivalent to parseInt in JS
# float converts to decimal
#import math
print(sum([1,2,3,4,5,6]))
print(max([1,2,3,4,5,6]))
print(min([1,2,3,4,5,6]))

# import random 


choice = random.choice(["Red", "Green", "Blue", "Yellow"])

num = list(range(10))
total = sum(num)
m= max(num)
# for n in num:
#     if n%2==0:
#         print (f"{n} is an even number")
#     else:
#         print (f"{n} is an odd number")
        

for n in num:
    new_num = int((n**m)/total)
    if new_num%2==0:
        print (f"{new_num} is an even number")
    else:
        print (f"{new_num} is an odd number")
        
print(choice)

# print(evaluate(10))

nums = range(1, num, 2)  # allows you to specify a starting point and the 3rd argument allows you to jump steps







































