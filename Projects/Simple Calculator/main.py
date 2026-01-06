a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))

print("What kind of action do you want to perform??\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division.")

opr = (input("Enter the operation: "))

match opr:
    case "+":
        print(f"{a} + {b} = {a+b}")
    case "-":
        print(f"{a} - {b} = {a-b}")
    case "*":
        print(f"{a} * {b} = {a*b}")
    case "/":
        print(f"{a} / {b} = {a/b}")
    case _:
        print("Invalid Choice")