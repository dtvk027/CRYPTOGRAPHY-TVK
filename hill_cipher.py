# Hill Cipher - 2x2
a = int(input("Enter k11: "))
b = int(input("Enter k12: "))
c = int(input("Enter k21: "))
d = int(input("Enter k22: "))

text = input("Enter plaintext: ").upper()

if len(text) % 2 != 0:
    text += "X"

encrypted = ""

for i in range(0, len(text), 2):
    x = ord(text[i]) - 65
    y = ord(text[i+1]) - 65

    e1 = (a*x + b*y) % 26
    e2 = (c*x + d*y) % 26

    encrypted += chr(e1 + 65) + chr(e2 + 65)

print("Encrypted:", encrypted)

det = (a*d - b*c) % 26
inv_det = pow(det, -1, 26)

i11 = (d * inv_det) % 26
i12 = (-b * inv_det) % 26
i21 = (-c * inv_det) % 26
i22 = (a * inv_det) % 26

decrypted = ""

for i in range(0, len(encrypted), 2):
    x = ord(encrypted[i]) - 65
    y = ord(encrypted[i+1]) - 65

    d1 = (i11*x + i12*y) % 26
    d2 = (i21*x + i22*y) % 26

    decrypted += chr(d1 + 65) + chr(d2 + 65)

print("Decrypted:", decrypted)
