def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice(1, 2, 3, 4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid choice. Please try again.")