import itertools

# def add(a, b):
#     return a+b

# print(add(2,3))


# # def addnum(*args, **kwargs):
# #     return sum(*args)

# # addnum(2,3)

# def listadd(x):
#     # x = int(x)
#     res = list(range(5))
#     print (res)
#     return res

# y = add(2,3)
# print(listadd(y))

# m= listadd(y)
# output = []
# sum = 0
# def cumulative(z):
    
#     for num in z:
#         sum += num
#         output.append(sum)
#     return output, len(output)

# print(cumulative(m))


#==================corrections =================

def add(x:int, y:int)->int:
    #Add two integers
    return x + y

def genList(total:int)-> list:
    #Returns a ilist of number range
    return list(range(total))

def cumList(items:list)->tuple([list, int]):
    cum = []
    for index, item in enumerate(items):
        sm = sum(items[:index+1])
        cum.append(sm)
    return len(cum), cum

def divCum(x,y)-> int:
    total = add(x,y)
    items = genList(total)
    length, cum = cumList(items)
    return sum(cum)// length

lastInt = divCum(2, 3)
print(lastInt)
assert(lastInt) == 4