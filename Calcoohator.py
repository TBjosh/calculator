import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Why are you trying to divide by zero?"
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Invalid input. Please enter a positive number."
    return math.sqrt(x)

def main():
    history = []
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Show History")
        print("9. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice == '8':
            print("\nCalculation History:")
            for record in history:
                print(record)
            continue

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = exponentiate(num1, num2)
            elif choice == '6':
                result = modulus(num1, num2)

            history.append(f"{num1} {choice} {num2} = {result}")
            print(f"The result is: {result}")

        elif choice == '7':
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

            result = square_root(num)
            history.append(f"sqrt({num}) = {result}")
            print(f"The result is: {result}")

        else:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()