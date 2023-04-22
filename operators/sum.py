#sum
a=10
b=20
print(a+b)
print(a+b-5)
#multiply
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)
#Equality comparison on floating point values

x = 1.1 + 2.2
print(x)
print(x==3.3)
tolerance = 0.0000001
print(abs(x-3.3) < tolerance)
print(abs(x-3.3))

#Logical Operators

print(~4)
print(~3)
print(~2)
print(~1)
print(~0)
print(~-4)
print(~-3)

print(callable(x))
print(callable(len))
print(callable(print))

print(not callable(x))
print(x<10 or callable(x))
print(x<10 and callable(x))

print(bool(0), bool(0.0))
print(bool(1.0), bool(-1.0))
print(bool(""), bool(" "), bool("f["))

print(type([]), type(()), type({}))

print(bool([1, 2, 3]), bool((1, 2, 3)), bool({1, 2, 3}), bool([]))

m = 3
n = 4 
print(m or n)
print(m and n)
print(n and m)

string =""
print(string or "default")


k = 1001
j = 100 + 1

print(k is not j)
print (k is j)
print(k == j)


num = [1, 2, 3, 4, 5]
print (2 in num)
print (6 in num)

print(5 is "5")
print (5 is not "5")