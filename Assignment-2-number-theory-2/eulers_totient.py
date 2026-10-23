n=int(input("Enter n: "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def phi(n): 
    c=0    
    for i in range(1,n):
        if gcd(n,i)==1:
            c+=1
    return c

print("euler's totient function for", n, "is", phi(n))