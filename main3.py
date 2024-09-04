#Simple Calculator

def add_cal(num1, num2):
    result = num1 + num2
    print(result)

def sub_cal(num1, num2):
    result = num1 - num2
    print(result)

def mul_cal(num1, num2):
    result = num1 * num2
    print(result)

def div_cal(num1, num2):
    result = num1 / num2
    print(result)

num1 = eval(input("Enter the first number: "))
op = input("Enter the operator (+, -, * or /): ")
num2 = eval(input("Enter the second number: "))

if op == "+":
    add_cal(num1, num2)
elif op == "-":
    sub_cal(num1, num2)
elif op == "*":
    mul_cal(num1, num2)
elif op == "/":
    div_cal(num1, num2)
else:
    print("Operator not available.")
