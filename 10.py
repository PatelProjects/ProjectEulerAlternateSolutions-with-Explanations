# # isPrime determines whether a given Integer is prime or not
# 
# def isPrime(n):
#     
#     # This function uses the fact that every prime number asides for 2 and 3 can be written in the 
#     # for 6n-1 or 6n+1 where n is natural number
#     
#     if n == 2: 
#         return True
#     if n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     if n % 3 == 0:
#         return False
#     
#     i = 5
#     w = 2
#     
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += w
#         w = 6 - w   
#     return True
# 
# 
# def sumOfPrimesBelow(n):
#     
#     # include the prime number 2 in the count so that we only have to check odd numbers
#     count = 2
#     
#     for i in range(3, n, 2):
#         if isPrime(i):
#             count += i
#             
#     return count
# 
# print(sumOfPrimesBelow(2000000))



# An alternate solution using the seive of eratosthenes

import math

# Determines the sum of all the primes below a given number
def sumOfPrimesBelow(n):
     
    # initialize the seive be allowing all numbers to be false (prime)
    seive = [False] * n
    
    # change all even numbers except to be true (composite)
    for i in range(4, n, 2):
        seive[i] = True
        
    # change multiples of every number upto the square root of n to be true (composite)
    for i in range(3, int(math.sqrt(n)), 2):
        if not seive[i]:
            for i in range (i + i, n, i):
                seive[i] = True
    
    # Now we are left with a seive of only prime number, so we sum them up
    
    sum = 0
    
    for i in range(2, n):
        if not seive[i]:

            sum += i
                
    return sum
    
print(sumOfPrimesBelow(2000000))


            