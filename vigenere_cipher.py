pt=input("Enter plaintext: ").upper()
key=input("Enter key: ").upper()
ct=""
j=0
for c in pt:
    if c.isalpha():
        k=ord(key[j%len(key)])-65
        ct+=chr((ord(c)-65+k)%26+65)
        j+=1
    else:
        ct+=c
print("Ciphertext:",ct)
dt=""
j=0
for c in ct:
    if c.isalpha():
        k=ord(key[j%len(key)])-65
        dt+=chr((ord(c)-65-k)%26+65)
        j+=1
    else:
        dt+=c
print("Decrypted:",dt)
