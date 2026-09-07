# Hill Cipher - 2x2

key = [[3, 3],
       [2, 5]]

# Modular inverse matrix for the above key modulo 26
inverse = [[15, 17],
           [20, 9]]

text = input("Enter 2-letter text: ").upper()
text = "".join(ch for ch in text if 'A' <= ch <= 'Z')

if len(text) != 2:
    print("Error: Enter exactly 2 letters.")
else:
    a = ord(text[0]) - ord('A')
    b = ord(text[1]) - ord('A')

    # Encryption
    e1 = (key[0][0] * a + key[0][1] * b) % 26
    e2 = (key[1][0] * a + key[1][1] * b) % 26

    encrypted = chr(e1 + ord('A')) + chr(e2 + ord('A'))

    # Decryption
    d1 = (inverse[0][0] * e1 + inverse[0][1] * e2) % 26
    d2 = (inverse[1][0] * e1 + inverse[1][1] * e2) % 26

    decrypted = chr(d1 + ord('A')) + chr(d2 + ord('A'))

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
