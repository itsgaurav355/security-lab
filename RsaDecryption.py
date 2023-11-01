# Input from the user
p = int(input("Enter the prime number p: "))
q = int(input("Enter the prime number q: "))
e = int(input("Enter the encryption exponent e: "))

# Calculate n and φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Calculate the modular multiplicative inverse of e modulo φ(n) to get the decryption exponent d
import sympy
d = sympy.mod_inverse(e, phi_n)

# Public key (n, e)
public_key = (n, e)

# Private key (n, d)
private_key = (n, d)

# Decryption (Example using c = ciphertext)
ciphertext = int(input("Enter the ciphertext to decrypt: "))
plaintext = pow(ciphertext, d, n)
print("Decrypted message:", plaintext)
