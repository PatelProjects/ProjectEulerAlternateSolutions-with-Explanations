# Consumes a natural number n and returns the sum of the numbers on the diagonals on an n by n matrix
def sumOfDiagonals(n):
    
    sum = 1
    current = 1
    
    count = 1
    
    # This question required recognizing the pattern of how the numbers on the diagonal are determined.
    # Once that is determined, they rest becomes straightforward
    while count <= (n-1)/2:
        for i in range(1, 5):
            current += 2*count
            sum += current
        count += 1
        
    return sum

print(sumOfDiagonals(1001))