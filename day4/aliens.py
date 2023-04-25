import random
import time
people = ["Ade", "Damian", "John", "Adamu", "Samson", "Moses", "David", "John", "Osaro", "Tube", "Tobe", "Nnanna", "Nnenna", "Mukaila"]



food = ["beer", "pizza", "chicken", "small-chops", "yam", "rice", "beans", "pap", "akara", "cake", "doughnut", "chips", "plantain"]

l = len(food)

consumed = []




# for f, i of enumerate(food):
#     index = random.randint(0, l-1)
#     if (index == i)





#------------------correction---------------


items_list = ["beer", "pizza", "chicken", "small-chops", "yam", "rice", "beans", "pap", "akara", "cake", "doughnut", "chips", "plantain"]

eaten = []
while len(items_list) > 0:
    
    index = random.randint(0, len(items_list)-1)
    eaten_item = items_list.pop(index)
    time.sleep(4)
    print(f"{eaten_item} is eaten")
    eaten.append(eaten_item)



































