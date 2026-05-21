text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string is:", reverse)