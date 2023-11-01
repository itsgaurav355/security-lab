def prime_checker(p):
    # Checks if the number entered is a Prime Number or not
    if p == 1:
        return -1
    elif p > 1:
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1
    return 1

def primitive_check(G, P):
    # Checks if the entered number is a Primitive Root or not
    l = []
    for i in range(1, P):
        l.append(pow(G, i) % P)
    for i in range(1, P):
        if l.count(i) > 1:
            l.clear()
            return -1
    return 1

l = []
while True:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime, please enter again!")
        continue
    break

while True:
    G = int(input(f"Enter the Primitive Root Of {P}: "))
    if primitive_check(G, P) == -1:
        print(f"Number is not a Primitive Root of {P}, please try again!")
        continue
    break

# Private Keys
x1 = int(input("Enter the Private Key of Alice: "))
x2 = int(input("Enter the Private Key of Bob: "))
while True:
    if x1 >= P or x2 >= P:
        print(f"Private Key of both users should be less than {P}!")
        continue
    break

# Calculate Public Keys
y1 = pow(G, x1, P)
y2 = pow(G, x2, P)

# Generate Secret Keys
k1 = pow(y2, x1, P)
k2 = pow(y1, x2, P)

print(f"Secret Key for Alice is {k1}\nSecret Key for Bob is {k2}\n")

if k1 == k2:
    print("Keys have been exchanged successfully")
else:
    print("Keys have not been exchanged successfully")

