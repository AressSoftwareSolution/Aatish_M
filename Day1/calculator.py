import csv

def calculation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error - (Division by zero)"
    else:
        return "Invalid Operator"

num1 = float(input("Enter the num1 value: "))
operator = input("Enter the operator [+ , -, *, /]: ")
num2 = float(input("Enter the num2 value: "))

Result = calculation(num1, num2,operator)

print("Result: ", Result)

expression = f"{num1} {operator} {num2} = {Result}"

with open("logs.csv", mode="a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([expression])

print("Calculations are successfully saved into logs.csv")
