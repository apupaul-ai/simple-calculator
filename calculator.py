import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Cannot find square root of a negative number."
    return math.sqrt(a)

def modulus(a, b):
    if b == 0:
        return "Error! Cannot find modulus with zero."
    return a % b


while True:
    print("\nCalculator Menu")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Modulus (%)")

    choice = input("Choose operation (1-7): ")

    try:
        if choice == "6":
            num1 = float(input("Enter number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error! Please enter valid numbers only.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", power(num1, num2))
    elif choice == "6":
        print("Result:", square_root(num1))
    elif choice == "7":
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid choice!")

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break