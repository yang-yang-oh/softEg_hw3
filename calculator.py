def calculate(a, b, operation):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    return result

print(calculate(10, 5, "add"))
print(calculate(10, 5, "subtract"))
print(calculate(10, 5, "multiply"))