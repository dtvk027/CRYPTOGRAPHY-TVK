# Playfair Cipher
# Fixed 5x5 matrix from the original program. J is treated as I.

matrix = [
    ['M', 'O', 'N', 'A', 'R'],
    ['C', 'H', 'Y', 'B', 'D'],
    ['E', 'F', 'G', 'I', 'K'],
    ['L', 'P', 'Q', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Z']
]

def position(ch):
    if ch == 'J':
        ch = 'I'

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

    return None

s = input("Enter 2 letters: ").upper()

if len(s) != 2 or not all('A' <= ch <= 'Z' for ch in s):
    print("Error: Enter exactly 2 letters.")
else:
    p1 = position(s[0])
    p2 = position(s[1])

    if p1 is None or p2 is None:
        print("Error: Invalid character.")
    else:
        r1, c1 = p1
        r2, c2 = p2

        # Encryption
        if r1 == r2:
            e1 = matrix[r1][(c1 + 1) % 5]
            e2 = matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            e1 = matrix[(r1 + 1) % 5][c1]
            e2 = matrix[(r2 + 1) % 5][c2]
        else:
            e1 = matrix[r1][c2]
            e2 = matrix[r2][c1]

        encrypted = e1 + e2
        print("Encrypted:", encrypted)

        # Decryption
        r1, c1 = position(e1)
        r2, c2 = position(e2)

        if r1 == r2:
            d1 = matrix[r1][(c1 - 1) % 5]
            d2 = matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            d1 = matrix[(r1 - 1) % 5][c1]
            d2 = matrix[(r2 - 1) % 5][c2]
        else:
            d1 = matrix[r1][c2]
            d2 = matrix[r2][c1]

        print("Decrypted:", d1 + d2)
