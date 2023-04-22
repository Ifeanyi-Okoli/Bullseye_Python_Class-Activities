count=0
arr=["a","e","i","o","u"]
str="ertyoynsndywoemnr"
for char in str:
    if(char in arr):
        count+=1
print (count)

#other methods
def getCount(str):
    return sum(c in "aeiou" for c in str)