# Luckily for us the permutations function from the itertools library returns permutations to us
# in lexicographic order.

from itertools import permutations

perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

output = ""

for i in perms[999999]:
    output += str(i)

print(output)
