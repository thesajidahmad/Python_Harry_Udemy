# 2. Match Case Statements

# Write a program using match case that simulates a simple calculator.
# 1. Ask the user for two numbers and an operation (+, -, *, /).
# 2. Perform the operation using match case .

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
oper = str(input("Enter (+, -, *, /): "))

match oper:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)