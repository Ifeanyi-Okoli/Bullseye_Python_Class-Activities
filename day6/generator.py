def generatorFunc():
    for num in range(10):
        yield num
print(x for x in range(10))

gr = (x for x in range(10))  #shorthand way of writing a generator function
print(gr)
print(next(gr))
print(next(gr))
print(next(gr))