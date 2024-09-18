
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def lcm(x, y):
    return abs(x * y) // gcd(x, y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
