def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    while True:
        # Display available operations
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        # Get user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")
        
        # Exit if the user chooses 5
        if choice == '5':
            print("Exiting the calculator.")
            break

        # Check if the choice is valid
        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice. Please select a valid operation.")
            continue

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        # Display the result
        print(f"The result is: {result}")

# Run the calculator function if this script is executed directly
if __name__ == "__main__":
    calculator()
