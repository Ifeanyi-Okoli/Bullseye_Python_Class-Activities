name = "house for sale"

print(type(name))
print(name.center(8, "*"))
print(name.center(100, "-"))
print(name.istitle())
print(name.isdigit())
print(name.endswith("sale"))
print(name.strip())
print(name.replace("0", "a"))
table = str.maketrans("a", "e")
print(table)
print(name.translate(table))



name2 = "ab\nrac\nadded"
name1 = "abracadabra"
print(name[:4])
print(name[-4:])
print(name[::-1])
print(name[::1])
print(name.splitlines())  #splits by new line
print(len(name))






comment = "the red fox jumped over the brown dog"
arr = comment.split(" ")
print(arr)
for i in arr:
    word = i.split("")
    for w, index in enumerate(word):
        if index == 0 | index == 1:
            w.upper()
        else:
            w*2
    str_word = word.join("")
str_arr = arr.join(" ")
print(str_arr)


























































