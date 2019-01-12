# getProduct consumes a natural number n and finds the product of values a, b and c such that
# the pythagorean identity is satisfied
def getProduct(n):
    # We can assume that a < b < c and so only need to check values upto c and b in the 
    # following loops respectively
    for c in range (1, n-1):
        for b in range(1, c):
            for a in range(1,b):
                if a + b + c == n and a**2 + b**2 == c**2:
                    print(a*b*c)
                    break
                
print(getProduct(1000))