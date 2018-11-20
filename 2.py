# Following variables define the base case of the recursive sequence
first = 1
second = 2

# Total keeps track of the sum of the even values in the sequence
total = 2

# Use the base case to recurse using the recursive algorithm until an upperbound of 4000000 is reached
while second < 4000000:
    memory = second
    second =  second + first
    first = memory
    
    # Add to total if current term is even
    if second % 2== 0:
        total += second
        
print(total)

# returns 4613732