import math

def calculator():
    print("Welcome to the Calculator!")
    while True:
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (^)")
        print("7. Square Root (√)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ['7']:
            num = float(input("Enter a number: "))
            print(f"Result: {math.sqrt(num)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")
            elif choice == '5':
                print(f"Result: {num1 % num2}")
            elif choice == '6':
                print(f"Result: {num1 ** num2}")
            else:
                print("Invalid choice. Please try again.")

calculator()