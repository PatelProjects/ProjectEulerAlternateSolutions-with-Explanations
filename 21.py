# divisors consumes a number and returns the sum of the numbers divisors
def divisorSum(n):
    sum = 1

    i = 2
    
    # We only need to check up until the square root of the number
    while i * i <=  n:
        if n % i == 0:
            
            sum += i + n // i
           
        i += 1
    
    if i * i == n:
        sum += i
    
    return sum

# consumes a natural number n adn returns the sum of all amicable natural numbers below n
def sumOfAmicable(n):
    div = [divisorSum(i) for i in range(0, n)]
    
    sum = []
    
    for i in range(1, n):
        if div[i] <= n-1 and div[i] != i:
            if div[div[i]] == i:
                sum.append( i)
                
    return sum

print(sum(sumOfAmicable(10000)))
