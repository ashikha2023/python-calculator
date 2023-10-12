# math_operations.py

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

# Call the functions with x = 300 and y = 4
x = 300
y = 4

add_result = add(x, y)
subtract_result = subtract(x, y)
multiply_result = multiply(x, y)
divide_result = divide(x, y)

# You can use the results or further process them as needed
