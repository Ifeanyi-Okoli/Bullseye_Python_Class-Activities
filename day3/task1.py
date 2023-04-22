main = "banana"
fruits=["mango", "apple", "banana", "grapes", "orange"]
#def basket(fruits):
for fruit in fruits:
    if fruit == main:
        print (f"{main} is among the fruits i bought")
        break
    else:
        continue
print (f"{main} is not among the fruits i bought")
   


words ="dhforoeemdnjtdoprr"
vowels = "aeiou"
count =0
for word in words:
    if word in vowels:
        count +=1
print (count)