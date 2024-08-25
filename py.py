def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            A = float(input("Enter first number: "))
            B = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(A, "+", B, "=", add(A, B))

        elif choice == '2':
            print(A, "-", B, "=", subtract(A, B))

        elif choice == '3':
            print(A, "/", B, "=", divide(A, B))

        elif choice == '4':
            print(A, "*", B, "=", multiply(A, B))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
