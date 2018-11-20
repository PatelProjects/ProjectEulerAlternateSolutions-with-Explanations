# n contains the number for which we are trying to find the largest prime factor of
n = 600851475143
i = 2

# Manipulate b be dividing by its prime factors until it can be divided by factors no longer,
# and so we obtain the greatest prime factor
while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1
    
print (n)

# returns 6857.0