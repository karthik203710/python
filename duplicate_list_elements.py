my_list = [10, 20, 30, 20, 40, 10, 50]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements are:", duplicates)