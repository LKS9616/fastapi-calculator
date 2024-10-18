def calculate(operation: str, num1: float, num2: float) -> float:
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operation")

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2