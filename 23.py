# sumOfDiv consumes a number and returns the sum of the numbers divisors
def sumOfDiv(n):
    sum = 1

    i = 2
    
    # We only need to check up until the square root of the number
    while i * i <  n:
        if n % i == 0:
            
            sum += i + n // i
           
        i += 1
    
    if i * i == n:
        sum += i
        
    return sum

# consumes a natural number n and returns the sum of all the natural numbers below n that cannot
# be written as the sum of two abundant numbers
def nonAbunSum(n):
    
    Abuns = []
    
    for i in range(6, 28123-6):
        if sumOfDiv(i) > i:
            Abuns.append(i)
                 
    nonAbunsSums = [True] * (n+1)
    
    for i in range (0, len(Abuns)):
        for j in range (i, len(Abuns)):
            if Abuns[i] + Abuns[j] <= n:
                nonAbunsSums[Abuns[i]+Abuns[j]] = False
      
    sum = 0
              
    for i in range(0, n+1):
        if nonAbunsSums[i]:
            sum += i
    return sum

print (nonAbunSum(28189))
    
        
            