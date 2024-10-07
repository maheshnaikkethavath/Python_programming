def gcd(a,b):
    while b:
           a, b = b, a % b
           return abs(a)
print(gcd(56, 98))
print(gcd(56, 98))  #