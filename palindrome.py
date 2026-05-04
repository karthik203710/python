text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("The string is a Palindrome")
else:
    print("The string is Not a Palindrome")