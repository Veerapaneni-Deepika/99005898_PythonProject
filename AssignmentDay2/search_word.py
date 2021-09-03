import re

file = open("C:/Users/Mounika Veerapaneni/Documents/sample.txt", "r")
readfile = file.read()
result = re.search(r'Hello',readfile)
print(result)