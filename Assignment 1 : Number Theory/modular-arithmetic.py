x = int(input("Enter the dividend: "))
y = int(input("Enter the divisor: "))
r = y
while (r!=0):
    q = x//y
    r = x%y
    print(x, " = ", y,"x", q,"+", r)
    x = y
    y = r
print("GCD is: ", x)
