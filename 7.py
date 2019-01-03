# isPrime determines whether a given Integer is prime or not

def isPrime(n):
    
    # This function uses the fact that every prime number asides for 2 and 3 can be written in the 
    # for 6n-1 or 6n+1 where n is natural number
    
    if n == 2: 
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    
    i = 5
    w = 2
    
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w   
    return True

# Returns the nth prime
def findNthPrime(n):
    count = 0
    
    i = 2
    
    while count !=  n:
        if isPrime(i):
            count += 1
            
        i+= 1
        
    return i-1
    
print(findNthPrime(10001))
    