# Columnar Transposition Cipher

text = input("Enter text: ").replace(" ", "").upper()

key = [3, 1, 4, 2]
cols = len(key)

if text:
    rows = (len(text) + cols - 1) // cols
else:
    rows = 0

# Fill the matrix row-wise. X is used as padding.
matrix = []
k = 0

for i in range(rows):
    row = []
    for j in range(cols):
        if k < len(text):
            row.append(text[k])
            k += 1
        else:
            row.append('X')
    matrix.append(row)

# Encryption
encrypted = ""

for number in range(1, cols + 1):
    column = key.index(number)
    for row in range(rows):
        encrypted += matrix[row][column]

print("Encrypted:", encrypted)

# Decryption
dec_matrix = [['' for _ in range(cols)] for _ in range(rows)]
k = 0

for number in range(1, cols + 1):
    column = key.index(number)
    for row in range(rows):
        dec_matrix[row][column] = encrypted[k]
        k += 1

decrypted = ""

for row in range(rows):
    for column in range(cols):
        decrypted += dec_matrix[row][column]

print("Decrypted:", decrypted)
