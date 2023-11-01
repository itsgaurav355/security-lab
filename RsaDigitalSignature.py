# To find d's value using Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0 = m
    t1, t2 = 0, 1
    if m == 1:
        return 0
    while m > 1:
        q = m // a
        a, m = m % a, a
        t2, t1 = t1 - q * t2, t2
        if t1 < 0:
            t1 += m0
    return t1

# To generate public and private key
def generate_keypair(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# To encrypt
def encrypt(private_key, m):
    d, n = private_key
    s = pow(m, d, n)
    return s

# To Verify sign.
def verify_sign(public_key, s):
    e, n = public_key
    m2 = pow(s, e, n)
    return m2

p = int(input("Enter value of p:"))
q = int(input("Enter value of q:"))
e = int(input("Enter value of e:"))
public_key, private_key = generate_keypair(p, q, e)
print("Public key: ", public_key)
print("Private key: ", private_key)
m1 = int(input("Enter message:")) # Numerical value

# To check m1 == m2
if encrypt(private_key, m1) == verify_sign(public_key, encrypt(private_key, m1)):
    print("The message is authentic")
else:
    print("Message is altered")
