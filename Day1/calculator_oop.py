import csv

class Calculator:
    
    def __init__(self, log_file="logs_oop.csv"):
        self.log_file = log_file

    def calculate(self, num1, num2, operator):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error - (Division by zero)"
        else:
            result = "Invalid Operator"
        self.log_calculation(num1, num2, operator, result)
        return result

    def log_calculation(self, num1, num2, operator, result):
        expression = f"{num1} {operator} {num2} = {result}"
        with open(self.log_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expression])



calc = Calculator()


num1 = float(input("Enter the num1 value: "))
operator = input("Enter the operator [+ , -, *, /]: ")
num2 = float(input("Enter the num2 value: "))


result = calc.calculate(num1, num2, operator)

print("Result:", result)
print(f"Calculation logged successfully in {calc.log_file}")
