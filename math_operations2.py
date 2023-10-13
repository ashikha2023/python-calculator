import sys

def add(x, y):
    result = x + y
    print(f"Addition: {x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    print(f"Subtraction: {x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    print(f"Multiplication: {x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        print("Division by zero is not allowed")
        return None
    result = x / y
    print(f"Division: {x} / {y} = {result}")
    return result

# Check if the correct number of command-line arguments are provided (2 in this case).
if len(sys.argv) != 3:
    print("Usage: python math_operations.py <X> <Y>")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    add_result = add(x, y)
    subtract_result = subtract(x, y)
    multiply_result = multiply(x, y)

    if y == 0:
        print("Division by zero is not allowed")
        sys.exit(1)

    divide_result = divide(x, y)

except ValueError:
    print("X and Y must be integers.")
    sys.exit(1)
