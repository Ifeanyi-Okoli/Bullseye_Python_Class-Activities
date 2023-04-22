comment = "the red fox jumped over the brown lazy dog"
arr = comment.split(" ")
# print(arr)
for i in arr:
    word = list(i)
    # print(word)
    for w, index in enumerate(word):
        if index == 0 or index == 1:
            w[index]=w.upper()
        else:
            w[index]=w*2
    str_word = " ".join(word)
str_arr = " ".join(arr)
print(str_arr)

#--------------correction--------------------

new = ""

comment_arr = comment.split(" ")
for word in comment_arr:
    first_two_letters = word[:2].upper()

    rest_letters = word[2:]
    doubld_letter = ""
    for letter in rest_letters:
        double_letter += letter * 2
    new += first_two_letters + doubled_letter + " "
#or
word = word[:2].upper() + "".join([letter*2 for letter in word[2:]])          
new += word + " "
print(new)