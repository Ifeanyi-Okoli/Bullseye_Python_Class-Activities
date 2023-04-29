"""declare five variables with the values of empty set, dictionary, list, using the constructors
Write a recursive function that returns the sum of any list passed into it."""

def setvar():
    empty_set = set()
    empty_dict = dict()
    empty_list = list()
    empty_tuple = tuple()
    return empty_set, empty_dict, empty_list, empty_tuple

print(setvar())

sum = 0
def recursv(arr):
    global sum
    if len(arr) == 0:
        return sum
    else:
        sum += arr[0]
        return recursv(arr[1:])    



print(recursv([1,2,3,4,5,6,7,8,9,10]))