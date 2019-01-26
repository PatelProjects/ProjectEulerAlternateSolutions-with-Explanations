# Another self explanatory one-line solution
import math
def factorialSum(n):
    return (sum([int(i) for i in str(math.factorial(n))]))

print(factorialSum(100))