import csv
import os

# path = os.getcwd()
# print(path)
with open("annual.csv", "r") as file:
    csvFile = csv.reader(file)
    
    print(csvFile)
    headers = next(csvFile)
    print(headers)
    
    for row in csvFile:
        year, *_the_rest = row
        if year == "2021":
            print(year)
