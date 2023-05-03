data = []
print("Tell me about your self. Enter 'quit' when done.")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break

finalText = '\n'.join(data)
print("\n, Your text is: ")
print(finalText)

name = input("What is your name? ")