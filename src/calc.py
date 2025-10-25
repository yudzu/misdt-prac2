def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

# some new features

if __name__ == "__main__":
    print("Example:", divide(10, 2))
