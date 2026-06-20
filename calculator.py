# Calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def squared(a,b):
    return a * a

print("Welcome to the Simple, Basic, No-Nonsense Calculator")
print("What would you like to do?")
print("A - Add two numbers together")
print("B - Subtract one number from another")
print("C - Multiply two numbers by  each other")
print("D - Divide one number by another")
print("E - Multiply one number by itself")

calc_choice = input("Enter choice: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if calc_choice == "A":
    print("Added: ", add(a,b))
elif calc_choice == "B":
    print("Subtracted: ", subtract(a,b))
elif calc_choice == "C":
    print("Multiplied: ", multiply(a,b))
elif calc_choice == "D":
    print("Divided: ", divide(a,b))
elif calc_choice == "E":
    print("Squared: ", squared(a,b))
else:
    print("Invalid choice")

