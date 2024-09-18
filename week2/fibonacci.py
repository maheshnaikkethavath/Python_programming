
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

a, b = 0, 1
count = 0

while count < num_terms:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
