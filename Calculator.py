def calculator():

    # Step 1: Ask the user to input the first number
    num1 = float(input("Enter the first number: "))

    # Step 2: Time to include some math operators! Let's compute the +, -, *, and /.
    operator = input("Enter the operator (+, -, *, /): ")

    # Step 3: Ask the user to input the second number
    num2 = float(input("Enter the second number: "))

# Add values
    if operator == "+":
        result = num1 + num2

# Subtract values
         elif operator == "-":
            result = num1 - num2

# Multiple values            
            elif operator == "*":
            result = num1 * num2

# Divide values            
             elif operator == "/":
                if num2 != 0:
                result = num1 / num2

# Show the user the output of the calculated sum               
             else:
                    print("Error: Division by zero!")
                    return
            else:
                print("Error: Invalid operator!")
            print(f"{num1} {operator} {num2} = {result}")
            
    calculator()            
