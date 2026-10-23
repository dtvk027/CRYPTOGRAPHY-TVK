a1=int(input("Enter a1:"))
n1=int(input("Enter n1:"))
a2=int(input("Enter a2:"))
n2=int(input("Enter n2:"))
a3=int(input("Enter a3:"))
n3=int(input("Enter n3:"))

def inverse(a, p):
    a = a % p          
    return pow(a, p-2, p)

N=n1*n2*n3
N1=N//n1
N2=N//n2
N3=N//n3

M1 = inverse(N1, n1)
M2 = inverse(N2, n2)
M3 = inverse(N3, n3)

print("M1=",M1)
print("M2=",M2)
print("M3=",M3)

x=(a1*N1*M1+a2*N2*M2+a3*N3*M3)%N
print("The solution is x=",x)
