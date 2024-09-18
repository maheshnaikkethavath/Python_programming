import sys
if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
result = num1 + num2

print(f"The sum of {num1} and {num2} is: {result}")
