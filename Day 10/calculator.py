import assets as asset

print(asset.logo)
def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return round(num1 / num2,4)

while True:
    num1 = float(input("What is the first number?: "))
    while True:
        operator = input("Pick an operator: +, -, *, or /: ")
        num2 = float(input("What is the second number?: "))

        if operator == "+":
            num1 = add(num1,num2)
        elif operator == "-":
            num1 = subtract(num1,num2)
        elif operator == "*":
            num1 = multiply(num1,num2)
        elif operator == "/":
            num1 = divide(num1,num2)
        else:
            print("Invalid operator. Please try again.")

        print(f"The answer is {num1}")

        should_continue = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ")

        if should_continue == "n":
            break
