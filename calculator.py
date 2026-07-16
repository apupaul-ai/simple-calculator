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


history = []   # ekhane shob calculation store hobe

while True:
    print("\nCalculator Menu")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Modulus (%)")
    print("8. Show History")

    choice = input("Choose operation (1-8): ")

    if choice == "8":
        if len(history) == 0:
            print("No calculations yet.")
        else:
            print("\n--- Calculation History ---")
            for item in history:
                print(item)
        again = input("\nDo you want to continue? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for using the calculator!")
            break
        continue

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
        result = add(num1, num2)
        history.append(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        history.append(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        history.append(f"{num1} * {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        history.append(f"{num1} / {num2} = {result}")
    elif choice == "5":
        result = power(num1, num2)
        history.append(f"{num1} ** {num2} = {result}")
    elif choice == "6":
        result = square_root(num1)
        history.append(f"sqrt({num1}) = {result}")
    elif choice == "7":
        result = modulus(num1, num2)
        history.append(f"{num1} % {num2} = {result}")
    else:
        print("Invalid choice!")
        continue

    print("Result:", result)

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break