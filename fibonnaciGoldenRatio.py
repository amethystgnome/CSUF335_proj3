# Author: Aubrianna Sample
# The purpose of this program is to calculate the fibonacci numbers
# to user's input using the golden ratio approach.

import math  # We need the math library for the sqrt function and pow function.

def fibonacci_golden_n(p, n):
    # Check if the input is valid.
    if not (isinstance(p, int) and isinstance(n, int) and p > 0):
        return "p should be a positive integer"
    # The golden ratio (phi) is calculated.
    phi = (1 + math.sqrt(5)) / 2  
    # Compute the pth Fibonacci number using the golden ratio.
    f_p = (pow(phi, p) - pow(1 - phi, p)) / math.sqrt(5)
    # Multiply the pth Fibonacci number with phi raised to the nth power and round it.
    return round(f_p * pow(phi, n))  

def fibonacci_golden_next(f_p):
    # The golden ratio (phi) is calculated.
    phi = (1 + math.sqrt(5)) / 2
    # Multiply the given Fibonacci number with the golden ratio and round it.
    return round(f_p * phi)  

# Take the user inputs for p and n.
p = int(input("Enter a positive integer for p: "))
n = int(input("Enter a positive integer for n: "))
# Print the result of fibonacci_golden_n function.
print(fibonacci_golden_n(p, n))  

# Take the user input for the previous term of the Fibonacci sequence.
f_p = float(input("Enter the previous term of the Fibonacci sequence (f or p): "))
# Print the result of fibonacci_golden_next function.
print(fibonacci_golden_next(f_p))  

# Print the first 20 terms of the Fibonacci sequence.
print("First 20 terms of the sequence:")
for i in range(20):
    print(fibonacci_golden_n(1, i))  

# Print the comparison of Eq. (4) and Eq. (5) for the first 20 terms of the Fibonacci sequence.
print("\nComparing outputs of Eq. (4) and Eq. (5)")
print("n", "Eq. (4)", "Eq. (5)")
f_p = 1
for n in range(20):
    f_n = fibonacci_golden_n(1, n)
    print(n, f_n, f_p)
    f_p = fibonacci_golden_next(f_p)

# Print the ratio of two consecutive Fibonacci numbers for the first 20 terms.
print("\nChecking the max:")
for n in range(1, 20):
    f_n = fibonacci_golden_n(1, n)
    f_np1 = fibonacci_golden_n(1, n+1)
    ratio = f_np1 / f_n
    print("n =", n, ", ratio =", ratio)
5