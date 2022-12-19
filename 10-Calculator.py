# Calculator!
  
def add(a, b):
    return a + b
  
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(n1, n2, calc):
    if calc == "+":
        return add(n1, n2)
    if calc == "-":
        return subtract(n1, n2)
    if calc == "*":
        return multiply(n1, n2)
    if calc == "/":
        return divide(n1, n2)

resume = True
num1 = int(input("What's the first number?: "))

print("+ - * /")  
operation = input("Pick an operation (listed above): ")
num2 = int(input("What's the next number?: "))
result = calculate(num1, num2, operation)
response = input(f"{num1} {operation} {num2} is {result}.\nType 'y' to continue calculating with {result} or 'n' to start new calculation: ")

while resume:
    if response == "y":
        print("+ - * /")  
        operation = input("Pick an operation (listed above): ")
        num1 = result
        num2 = int(input("What's the next number?: "))
        result = calculate(num1, num2, operation)
        response = input(f"{num1} {operation} {num2} is {result}.\nType 'y' to continue calculating with {result} or 'n' to start new calculation: ")
    elif response == "n":
        num1 = int(input("What's the first number?: "))
        print("+ - * /")  
        operation = input("Pick an operation (listed above): ")
        num2 = int(input("What's the next number?: "))
        result = calculate(num1, num2, operation)
        response = input(f"{num1} {operation} {num2} is {result}.\nType 'y' to continue calculating with {result} or 'n' to start new calculation: ")
    elif response == "q":
        resume = False




    # if response == "n" or "no" or "No" or "NO":
    #     resume = False