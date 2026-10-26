p = int(input("Enter prime number: "))
g = int(input("Enter generator: "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)
print("Alice's shared key:", key1)
print("Bob's shared key:", key2)
