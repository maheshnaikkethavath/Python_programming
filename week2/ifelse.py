
char = input("Enter a character: ")


if char.isdigit():
    print("The input is a digit.")
elif char.islower():
    print("The input is a lowercase character.")
elif char.isupper():
    print("The input is an uppercase character.")
elif len(char) == 1:  
    print("The input is a special character.")
else:
    print("Invalid input.")
