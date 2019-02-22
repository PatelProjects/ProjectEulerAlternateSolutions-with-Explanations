# firstNDigits consumes a natural number n and returns the index of the first term in the fibonnacci sequence
# that contains n number of digits

def firstNDigits(n):
    sequence = [1, 1]
    
    while len(str(sequence[-1])) != n:
        sequence.append(sequence[-1] + sequence[-2])
        
    # The length of the sequence gives the index of the last term
    return (len(sequence))

print(firstNDigits(1000))