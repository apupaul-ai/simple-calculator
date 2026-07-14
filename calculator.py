import math

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
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)
    elif choice == "5":
        print("Result:", num1 ** num2)
    elif choice == "6":
        if num1 < 0:
            print("Error! Cannot find square root of a negative number.")
        else:
            print("Result:", math.sqrt(num1))
    elif choice == "7":
        if num2 == 0:
            print("Error! Cannot find modulus with zero.")
        else:
            print("Result:", num1 % num2)
    else:
        print("Invalid choice!")

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break