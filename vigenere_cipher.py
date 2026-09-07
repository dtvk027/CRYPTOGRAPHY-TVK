# Vigenere Cipher

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

# Keep only letters in the key
key = "".join(ch for ch in key if 'A' <= ch <= 'Z')

if not key:
    print("Error: Key must contain at least one letter.")
else:
    encrypted = ""
    key_index = 0

    for ch in text:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted += ch

    decrypted = ""
    key_index = 0

    for ch in encrypted:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted += ch

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
