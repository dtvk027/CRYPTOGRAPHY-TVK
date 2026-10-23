no=int(input("Enter the number of equations:"))
N=1
x=0
n=[]
a=[]
k=[]
m=[]
def inverse(a, p):
    a = a % p          
    return pow(a, p-2, p)
for i in range(no):
    a.append(int(input("Enter a:")))
    n.append(int(input("Enter n:")))

for i in range(no):
    N*=n[i]
for i in range(no): 
    k.append(N//n[i])
for i in range(no):
    m.append(inverse(k[i],n[i]))       

for i in range(no):
    x = (x + a[i] * k[i] * m[i]) % N

print("The solution is x =",x)
