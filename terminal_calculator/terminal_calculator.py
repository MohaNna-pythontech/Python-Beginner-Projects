def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "q":
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please a valid number. ")


def get_operator():
    valid_operators = ("+", "-", "*", "/")
    while True:
        operator = input("Enter operator (+, -, *,/) or q to quit: ")
        if operator == "q":
            return None
        if operator in valid_operators:
            return operator
        print("Error: Invalid operator.")


def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        try:
            return first_number / second_number
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."


while True:
    num1 = get_number("Enter first number (or q to quit): ")
    if num1 is None:
        break
    operator = get_operator()
    if operator is None:
        break
    num2 = get_number("Enter second number (or q to quit): ")
    if num2 is None:
        break
    result = calculate(num1, operator, num2)
    print(result)
