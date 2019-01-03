# diffBetween consumes a Natural number n and outputs the difference between the sum of the
# squares of all natural numbers upto and including n and the square of the sum of all natural 
# numbers upto and including n

def diffBetween(n):
    sumOfSquare = 0
    for i in range(1, n+1):
        sumOfSquare +=  i**2
        
    # Here we use the arithmetic series forumula to get the sum of the first n natural numbers
    return ((n+1)*n/2)**2 - sumOfSquare

print( diffBetween(100))