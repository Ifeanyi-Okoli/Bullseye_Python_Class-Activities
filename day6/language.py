def validate_hello(greetings):
    language = {
        "hello": "English",
        "ciao": "Italian",
        "salut": "French",
        "hola": "Spanish",
        "ahoj": "Czech Republic",
        "hallo": "German",
        "czesc": "Polish"
    }
    
    for i in language:
        if i == greetings:
            return True
        return False    

print(validate_hello("hello"))