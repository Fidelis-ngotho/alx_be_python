# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# Test block for standalone execution
if __name__ == "__main__":
    # Example test case
    result = perform_operation(10, 2, 'add')
    print(f"Test Result: {result}")
if __name__ == "__main__":
    print(f"Addition: {perform_operation(10, 2, 'add')}")
    print(f"Subtraction: {perform_operation(10, 2, 'subtract')}")
    print(f"Multiplication: {perform_operation(10, 2, 'multiply')}")
    print(f"Division: {perform_operation(10, 2, 'divide')}")
    print(f"Division by Zero: {perform_operation(10, 0, 'divide')}")
    print(f"Invalid Operation: {perform_operation(10, 2, 'modulus')}")
def perform_operation(num1, num2, operation):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    return operations.get(operation, "Error: Invalid operation")(num1, num2)
