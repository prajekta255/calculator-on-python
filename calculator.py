# Calculator with loop in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b


while True:
    print("\n----- Python Calculator -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponent ()")
    print("7. Floor Division (//)")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == '8':
        print("Exiting calculator... Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    elif choice == '6':
        print("Result:", exponent(num1, num2))
    elif choice == '7':
        print("Result:", floor_division(num1, num2))
    else:
        print("Invalid Input! Please try again.")