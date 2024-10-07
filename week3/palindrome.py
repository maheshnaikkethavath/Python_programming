def palindrome(s):
   
    normalized_s = ''.join(char.lower() for char in s if char.isalnum())

    return normalized_s == normalized_s[::-1]


print(palindrome("A man, a plan, a canal, Panama")) 
print(palindrome("hello"))                           
print(palindrome("Racecar"))                           
