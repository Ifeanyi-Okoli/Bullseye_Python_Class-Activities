import math


# def avg(*args):
#     for arg in args:
#         if type(arg) != int:
#             raise TypeError("Only integers are allowed")
#         else:
#             return sum(args) / len(args)
    

# print(avg(1, 2, 3, 4))

# print(avg(1, 2, 3,))

# print(avg(1, 2, 3, "4"))

#====================correction=============


def avg(*args):
    total = 0
    for num in args:
        if isinstance(num, int or float):
            total += num
        else:
            raise TypeError("Only integers are allowed")
    return total / len(args)