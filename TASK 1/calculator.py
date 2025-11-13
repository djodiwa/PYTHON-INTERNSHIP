def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Welcome to ~DIWA Simple CLI PYTHON Calculator!")

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == '5':
        print("Goodbye!")
        break
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid numbers!")
    else:
        print("Invalid choice!")