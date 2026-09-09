plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
text = input("Enter text: ").upper()
encrypted = ""
for ch in text:
    if ch in plain:
        encrypted += key[plain.index(ch)]
    else:
        encrypted += ch
decrypted = ""
for ch in encrypted:
    if ch in key:
        decrypted += plain[key.index(ch)]
    else:
        decrypted += ch
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
