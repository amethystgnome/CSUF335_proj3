# Author: Aubrianna Sample
# The purpose of this program is to calculate the fibonacci to 15 
# using exhaustive algorithmic pattern.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(15)) # Prints the 15th term of the sequence.