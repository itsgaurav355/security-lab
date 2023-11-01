import random
import math

# Take user input for p, q, and e
p = int(input("Enter the value of p (a prime number): "))
q = int(input("Enter the value of q (a prime number different from p): "))
e = int(input("Enter the value of e (a positive integer coprime to (p-1)*(q-1)): "))
M = int(input("Enter the plaintext message (an integer): "))

# Calculate n
n = p * q

# Calculate ϕ(n)
phi = (p - 1) * (q - 1)

# Verify that e is coprime with ϕ(n)
if math.gcd(e, phi) == 1:
    # Calculate the modular multiplicative inverse of e mod ϕ(n)
    d = pow(e, -1, phi)
    
    # Encryption
    C = pow(M, e, n)
    
    print(f"Public Key (n, e): ({n}, {e})")
    print(f"Private Key (n, d): ({n}, {d})")
    print(f"Encrypted Message: {C}")
else:
    print("e is not coprime with ϕ(n). Choose a different e.")
