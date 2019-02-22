# Consumes a natural number n and determines the length of the longest recurring cycle in 
# the fraction 1/n
def calculator(n):
    
    x = 1
    checked = []
    
    # The cycle is repeated when the number after the remainder borrows 10 (long division) has appeared
    # before, and so we keep track of these number and see when it repeats
    while True:
        if x in checked:
            break
        remainder = x % n
        checked.append(x)
        
        x = remainder * 10
        
    return len(checked)-1
   
# Now we simply test all the numbers between 1 and 1000

def reciprocolCycles(n):
    highest = 0   
    number = 0   
    for i in range(1,n):
        y = calculator(i)
        if y > highest:
            highest = y
            number = i
            
    return number

print (reciprocolCycles(1000))


