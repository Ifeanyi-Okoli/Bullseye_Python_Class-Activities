name = input("what is yur name  ")
num_age = int(input("How old are you? "))

num_apple = int(input("How manyapple do you eat in a day? "))

life_span = int(num_age * num_apple) * 0.7

comment = f"Hi {name}, You have {life_span} years longer to live"
print(comment)
comment = "Hi {}, You have {} years longer to live".format(name, life_span)
print(comment)

comment = "Hi %s, You have %s years longer to live" %(name, life_span)
print(comment)