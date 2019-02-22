# isPrime determines whether a given Integer is prime or not

def isPrime(n):
    
    # This function uses the fact that every prime number asides for 2 and 3 can be written in the 
    # for 6n-1 or 6n+1 where n is natural number
    
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0:
        return False
    
    i = 5
    c = 2
    
    while i * i <= n:
        if n % i == 0:
            return False
        i += c
        c = 6 - c
        
    return True

# Now we can simply brute force our way through all possibilities

highest = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        counter = 0
        
        # The counter also represents the n value, and so we not need a separate variable for it
        while isPrime(counter**2 + a*counter + b):
            counter += 1
        
        if counter > highest:
            highest = counter
            output = a * b 
            
print(output)
        
        