s=input("enter cipher text:")
for i in range(26):
    k=i
    d=[]
    for c in s:
        if c==" ":
            d.append(" ")
        else:
            y=(ord(c)-65-k)%26
            d.append(chr(y+97))
    for j in d:
        print(j,end="") 
    print("\n")