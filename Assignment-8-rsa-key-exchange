import math
p = int(input("Enter the first prime: "))
q = int(input("Enter the second prime: "))
n = p * q
phi = (p - 1) * (q - 1)
for e in range(2, phi):
    if math.gcd(e, phi) == 1:
        break
for d in range(2, phi):
    if (e * d) % phi == 1:
        break
m = int(input("Enter the message: "))
c = pow(m, e, n)
b = pow(c, d, n)
print("Encrypted:", c)
print("Decrypted:", b)
