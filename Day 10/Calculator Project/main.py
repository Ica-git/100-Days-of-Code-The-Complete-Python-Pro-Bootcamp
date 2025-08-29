from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


print(logo)

last_resault = None

while 1:

    if last_resault is not None:
        number1 = last_resault
    else:
        number1 = float(input("What is your first number? "))


    operator = input("+\n-\n*\n/\nPick an operator: ")

    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        continue

    """"
    
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    
    for symbol in operator:
        print(symbol)
    
    result = operations[operator](number1, number2)
    
    
    """


    number2 = float(input("What is your next number? "))

    result = 0
    if operator == "+":
        result = add(number1, number2)
    elif operator == "-":
        result = subtract(number1, number2)
    elif operator == "*":
        result = multiply(number1, number2)
    elif operator == "/":
        result = divide(number1, number2)



    print(f"{number1} {operator} {number2} = {result}")

    letter = input(f"Type 'y' to continue calculating with {result}, or "
                    f"type 'n' to start a new calculation: ")

    if letter == "y":
        last_resault = result
    elif letter == "n":
        last_resault = None
        continue
    else:
        print("Invalid input")
        last_resault = None
        continue


