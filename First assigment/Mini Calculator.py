print("Simple Calculator")

# Taking inputs
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Performing operation
if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid operation. Please enter +, -, * or /")