key=input("Enter key: ").upper().replace("J","I")
pt=input("Enter plaintext: ").upper().replace("J","I")
seen=""
for c in key+"ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if c not in seen and c.isalpha():
        seen+=c
m=[]
for i in range(5):
    m.append(list(seen[i*5:i*5+5]))
p=""
for c in pt:
    if c.isalpha():
        p+=c
prep=""
i=0
while i<len(p):
    x=p[i]
    y=p[i+1] if i+1<len(p) else "X"
    if x==y:
        prep+=x+"X"
        i+=1
    else:
        prep+=x+y
        i+=2
if len(prep)%2!=0:
    prep+="X"
ct=""
for i in range(0,len(prep),2):
    x=prep[i]
    y=prep[i+1]
    for r in range(5):
        for cc in range(5):
            if m[r][cc]==x:
                r1,c1=r,cc
            if m[r][cc]==y:
                r2,c2=r,cc
    if r1==r2:
        ct+=m[r1][(c1+1)%5]+m[r2][(c2+1)%5]
    elif c1==c2:
        ct+=m[(r1+1)%5][c1]+m[(r2+1)%5][c2]
    else:
        ct+=m[r1][c2]+m[r2][c1]
print("Ciphertext:",ct)
dt=""
for i in range(0,len(ct),2):
    x=ct[i]
    y=ct[i+1]
    for r in range(5):
        for cc in range(5):
            if m[r][cc]==x:
                r1,c1=r,cc
            if m[r][cc]==y:
                r2,c2=r,cc
    if r1==r2:
        dt+=m[r1][(c1-1)%5]+m[r2][(c2-1)%5]
    elif c1==c2:
        dt+=m[(r1-1)%5][c1]+m[(r2-1)%5][c2]
    else:
        dt+=m[r1][c2]+m[r2][c1]
print("Decrypted:",dt)
