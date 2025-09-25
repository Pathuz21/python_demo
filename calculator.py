# calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Example usage
if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Sub:", sub(10, 5))
    print("Mul:", mul(10, 5))
    print("Div:", div(10, 5))