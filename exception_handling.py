try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except ValueError:
    print("Error: Please enter valid numbers")