# Rail Fence Cipher - 2 Rails

text = input("Enter text: ").replace(" ", "").upper()

rail1 = ""
rail2 = ""

for i, ch in enumerate(text):
    if i % 2 == 0:
        rail1 += ch
    else:
        rail2 += ch

encrypted = rail1 + rail2
print("Encrypted:", encrypted)

mid = (len(text) + 1) // 2
r1 = encrypted[:mid]
r2 = encrypted[mid:]

decrypted = ""
i = 0
j = 0

while i < len(r1) or j < len(r2):
    if i < len(r1):
        decrypted += r1[i]
        i += 1
    if j < len(r2):
        decrypted += r2[j]
        j += 1

print("Decrypted:", decrypted)
