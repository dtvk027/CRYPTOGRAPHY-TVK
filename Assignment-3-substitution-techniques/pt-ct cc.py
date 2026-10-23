s=input("enter plain text:")
k=int(input("enter key:"))
l=[]
for p in s:
    if p==" ":
        l.append(" ")
    else:    
        x=(ord(p)-97+k)%26
        l.append(chr(x+65))
for i in l:
    print(i,end="") 


