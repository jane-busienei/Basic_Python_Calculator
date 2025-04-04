# Prompt the user to enter two numbers and operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, **, %, /): ")

'''Calculation success when conditions are met
Error handling incase of errors
'''

if operation == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == '**':
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")
elif operation == '%':
    if num2 == 0:
        print("Error: Error: Number not divisible by zero!")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Number not divisible by zero!")
else:
    print("Invalid operation! Please enter the one of the following operators +, -, *, or /.")