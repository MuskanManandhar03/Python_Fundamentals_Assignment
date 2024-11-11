def classify_number():
    while True:
        # Prompt the user to enter a number or type 'exit' to quit
        user_input = input("Enter a number (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Exiting the classification program.")
            break
        
        # Attempt to convert the input to a float (to handle decimals as well)
        try:
            number = float(user_input)
            
            # Classify the number
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
        
        # Handle invalid input that can't be converted to a number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Call the function
if __name__ == "__main__":
    classify_number()
