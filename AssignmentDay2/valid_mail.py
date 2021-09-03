import re

file1 = open("C:/Users/Mounika Veerapaneni\Documents/email.txt", "r")
for line in file1:
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    print(line)
    if(re.search(regex,line)):
        print("Valid Email")
    else:
        print("Invalid Email")