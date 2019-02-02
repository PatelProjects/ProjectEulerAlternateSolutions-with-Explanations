names = open("C:/Users/Abhishek Patel/Desktop/p022_names.txt")

names = [i.strip('"') for i in names.readline().split(",")]
names.sort()

import string

# Creates a list of the capital letters of the alphabet, in order of numerical value
letters = [i for i in string.ascii_uppercase]

sum = 0

for name in range(0, len(names)):
    strName = str(names[name])
    for letter in strName:
        
        # Add 1 to account for arrays beginning at index 0
        sum += (1 + letters.index(letter)) * (1 + name)

print(sum)
