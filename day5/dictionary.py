#create dictionary to check meaning of words

dictionary = {
    "come": "to move towards a place or person",
    "extend": "to make something longer or wider",
    "cook": "to prepare food by heating it",
}


def get_meaning(word):
    match word:
        case "come":
            print(f"{dictionary.get(word)}")
        case "extend":
            print(f"{dictionary.get(word)}")
        case "cook":
            print(f"{dictionary.get(word)}")
        case _:
            print("word not found")
    # return dictionary.get(word, "word not found")

print (get_meaning("extend"))


#=============corection=============

words = { 
       "Museum": "A place where artefacts are kept",
        "come": "to move towards a place or person",
        "extend": "to make something longer or wider",
        "cook": "to prepare food by heating it", 
    }





def checkMeaning(word):
    match word:
        case word if word in words:
            print(f"{word} means {words[word]}")
            return (f"{word} means {words[word]}")

print (checkMeaning("extend"))

























