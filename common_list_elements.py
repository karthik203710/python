list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements are:", common)