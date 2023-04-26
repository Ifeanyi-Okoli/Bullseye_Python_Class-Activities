# lambda # we use lambda for anonymous function

# cal = lambda x:x**2

# print(cal(2))

# cal =  map(lambda x,y: x**y, [(x, y) for x, y in enumerate(range(20))])

# print(list(cal))

#anonymous function that will be used in a map to return all odd numbers in range of 10

odd = filter(lambda x:   x%2 != 0, range(10))
print(list(odd))