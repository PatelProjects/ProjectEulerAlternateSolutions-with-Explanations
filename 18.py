# Create an array to hold the levels of the tree
p = []

p.append([75])
p.append([95, 64])
p.append([17, 47, 82])
p.append([18, 35, 87, 10])
p.append([20, 4, 82, 47, 65])
p.append([19, 1, 23, 75, 3, 34])
p.append([88, 2, 77, 73, 7, 63, 67])
p.append([99, 65, 4, 28, 6, 16, 70, 92])
p.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
p.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
p.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
p.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
p.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
p.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
p.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

# Reverses the array
p = p[::-1]

while len(p) != 1:
    # Here we create a new array containing the maximum value of the bottom 2 levels of the tree
    # We remove the 2 combined levels from the array and insert this new array as the bottom-most level instead
    maxList = [max(p[1][i] + p[0][i], p[1][i] + p[0][i+1]) for i in range(0, len(p[1]))]

    del p[0]
    del p[0]
 
    p.insert(0, maxList)
    
print(p[0][0])