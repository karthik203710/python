my_list = [40, 10, 30, 20, 50]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

print("Sorted list:", my_list)