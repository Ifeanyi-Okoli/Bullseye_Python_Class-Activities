comment = "the red fox jumped over the brown lazy dog"
arr = comment.split(" ")
newWord = ""
for i in arr:
    word = list(i)
    for index, w in enumerate(word):
        if index == 0 or index == 1:
            newWord +=w.upper()
        else:
            newWord += w*2
        # print(newArr)
    newWord += " "    
    str_word = "".join(newWord)
str_arr = "".join(str_word)
print(str_arr)

#--------------correction--------------------

new = ""

comment_arr = comment.split(" ")
for word in comment_arr:
    first_two_letters = word[:2].upper()

    rest_letters = word[2:]
    doubled_letter = ""
    for letter in rest_letters:
        doubled_letter += letter * 2
    new += first_two_letters + doubled_letter + " "
print(new) 
   
#or
for word in comment_arr:
    word = word[:2].upper() + "".join([letter*2 for letter in word[2:]])          
    new += word + " "
print(new)