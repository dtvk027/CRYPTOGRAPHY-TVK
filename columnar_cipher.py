pt=input("Enter plaintext: ").replace(" ","")
key=input("Enter key: ")
k=len(key)
order=sorted(range(k),key=lambda x:key[x])
while len(pt)%k!=0:
    pt+="X"
rows=len(pt)//k
grid=[pt[i*k:i*k+k] for i in range(rows)]
ct=""
for col in order:
    for row in grid:
        ct+=row[col]
print("Ciphertext:",ct)
cols=[""]*k
idx=0
for pos,col in enumerate(order):
    cols[col]=ct[idx:idx+rows]
    idx+=rows
dt=""
for i in range(rows):
    for col in cols:
        dt+=col[i]
print("Decrypted:",dt)
