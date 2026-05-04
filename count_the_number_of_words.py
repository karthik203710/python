file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Number of words in the file:", len(words))

file.close()