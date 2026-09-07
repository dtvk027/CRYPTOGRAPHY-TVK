# Caesar Cipher

text = input("Enter text: ")
shift = int(input("Enter shift: "))

encrypted = ""

for ch in text:
    if 'A' <= ch <= 'Z':
        encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += ch

decrypted = ""

for ch in encrypted:
    if 'A' <= ch <= 'Z':
        decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += ch

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
