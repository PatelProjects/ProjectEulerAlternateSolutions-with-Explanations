import math

# We can ask ourselves the equivilant question: In how many ways can we rearrange a series of 40 (20 + 20) rights and downs

#changes in x + y 
totalCombinations = 40

redundancies = 20

print(   (math.factorial(totalCombinations))   //  (  (math.factorial(redundancies)) * (math.factorial(redundancies))  ) )