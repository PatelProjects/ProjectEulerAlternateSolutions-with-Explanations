# evenlyDivisible consumes a number and a dividend and determines if the number is divisible by all the numbers
# upto and including the dividend

def evenlyDivisible(number, dividend):
    # We only need to check the numbers above 10 because they confirm that the numbers below 10 are factors
    for i in range(10, dividend + 1):
        if not number % i == 0: 
            return False
    return True
        
# smallestMultiple consumes a dividend and determines the smallest number such that all natural numbers upto and
# including the dividend are factors

def smallestMultiple(dividend):
    # We can start at and count by 20 because it is a requirement that the number is divisible by 20
    counter = 20
    while not evenlyDivisible(counter, dividend):
        counter += 20
        
    return counter
   
   
print(smallestMultiple(20))     