"""This is our first file
We are going to be working with files going forward
"""
import os

print("file", os.getcwd())
file = open("comments.txt", "r")
content = file.read()
file.close()
print(content)

file.write = ("This is our first file")
file = open("comments.txt", "w")
