# Define a variable, sum, to keep track of the total sum of numbers that match the given criteria found so far
sum = 0

# Check each number between 1 and 1000 to see if it matches the given criteria
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        sum += i
print(sum)

# Returns 233168