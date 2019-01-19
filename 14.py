
cache = {1: 1}

# consumes a natural number and returns the length of the corresponding collatz chain produced
def collatz_count(n):
    if n not in cache:
        if n % 2 == 0:
            cache[n] = 1 + collatz_count(n / 2)
        else:
            cache[n] = 1 + collatz_count(3 * n + 1)
    return cache[n]

# consumes a natural number n and finds the length of the longest collatz chain generated
# by a natural upto n
def longestChainBelow(n):
    highest = 0 
    number = 0
    for i in range(1, n):
        x =  collatz_count(i)
        if x > highest:
            highest = x
            number = i
            
    return number

print(longestChainBelow(1000000))