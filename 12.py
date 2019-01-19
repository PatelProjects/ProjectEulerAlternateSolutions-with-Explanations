# Returns the total number of divisors for a given number n
def divisors(n):
    total = 1
    while n%2 == 0:
        n /= 2
        total += 1
    
    i = 3
    
    while i*i <= n:
        prime = 1 
        while n % i == 0:
            prime += 1
            n /= i
        
        total *= prime
        i += 2
    
    if n != 1:
        total *= 2
    
    return total


# produces the first triangle number with more than m divisors
def greaterThanMDivisors(m):
        
    n = 1
        
    while True:
        number = int(n*(n+1)/2)
               
        if divisors(number) > m:
            break
              
        n+= 1
    return number
    
print(greaterThanMDivisors(500))
    
