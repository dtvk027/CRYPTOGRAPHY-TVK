a=int(input("Enter a: ")) 
p=int(input("Enter p: "))

def prime(p):
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True
if prime(p)==True:
    print(p, "is prime")
    if a**(p-1)%p==1:
        print(a, "^^(p-1) is congruent to 1 mod. Hence, Fermat's Little Theorem holds for", p)
    else:
        print(a, "^^(p-1) is not congruent to 1 mod. Hence, Fermat's Little Theorem does not hold for", p)
else:
    print(p, "is not prime")