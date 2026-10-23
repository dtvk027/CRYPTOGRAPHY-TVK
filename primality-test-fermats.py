a=int(input("Enter a: ")) 
p=int(input("Enter p: "))

if a**(p-1)%p==1:
    print(a, "^^(p-1) is congruent to 1 mod and ", p, " is maybe prime. Hence, Fermat's Little Theorem holds for", p)
else:
    print(a, "^^(p-1) is not congruent to 1 mod and and ", p, " is not prime. Hence, Fermat's Little Theorem does not hold for", p)
