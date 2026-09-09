pt=input("Enter plaintext (even length): ").upper()
a=int(input("Enter key a11: "))
b=int(input("Enter key a12: "))
c=int(input("Enter key a21: "))
d=int(input("Enter key a22: "))
if len(pt)%2!=0:
    pt+="X"
ct=""
for i in range(0,len(pt),2):
    x=ord(pt[i])-65
    y=ord(pt[i+1])-65
    p=(a*x+b*y)%26
    q=(c*x+d*y)%26
    ct+=chr(p+65)+chr(q+65)
print("Ciphertext:",ct)
det=(a*d-b*c)%26
det_inv=pow(det,-1,26)
ia=(d*det_inv)%26
ib=(-b*det_inv)%26
ic=(-c*det_inv)%26
id_=(a*det_inv)%26
dt=""
for i in range(0,len(ct),2):
    x=ord(ct[i])-65
    y=ord(ct[i+1])-65
    p=(ia*x+ib*y)%26
    q=(ic*x+id_*y)%26
    dt+=chr(p+65)+chr(q+65)
print("Decrypted:",dt)
