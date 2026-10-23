a=int(input("Enter a: "))
n=int(input("Enter n: "))

def gcd(p, q):
    while q:
        p, q = q, p % q
    return p

def phi(n):
    c=0    
    for i in range(1,n):
        if gcd(n,i)==1:
            c+=1
    return c

print("euler's totient function for", n, "is", phi(n))
if a**phi(n) % n == 1:
    print(a, "^^phi(", n, ") is congruent to 1 mod", n)
else:
    print(a, "^^phi(", n, ") is not congruent to 1 mod", n)    
