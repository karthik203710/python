num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not Prime")
            break
    else:
        print("The number is Prime")
else:
    print("The number is not Prime")