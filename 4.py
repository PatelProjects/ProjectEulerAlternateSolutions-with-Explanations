# isPalinme consume a Natural number n and outputs wether or not it is a palindrome
def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

# Define a constant to store the largest palindrome found by the program so far
largest = 0

# check where the product of three-digit numbers form a palindrome and store the largest one found
for i in range(100, 1000):
    for j in range(100, i):
        if isPalindrome(i*j) and i*j > largest:
            largest = i*j
            

print (largest)