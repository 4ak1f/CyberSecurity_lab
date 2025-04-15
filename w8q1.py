from sage.all import *

# Define the number 'a' and prime 'p'
a = 7  # Example number
p = 13  # Example prime number

# Calculate the modular inverse
mod_inverse = inverse_mod(a, p)

print(f"The inverse of {a} modulo {p} is {mod_inverse}.")
