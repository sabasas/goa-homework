# You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.

# Here are the following valid operators :

# + Addition
# - Subtraction
# * Multiplication
# // Integer Division
def calculator(txt):
    left, operator, right = txt.split()
    num1 = len(left)
    num2 = len(right)

    if operator == "+":
        return "." * (num1 + num2)
    elif operator == "-":
        return "." * (num1 - num2)
    elif operator == "*":
        return "." * (num1 * num2)
    elif operator == "//":
        return "." * (num1 // num2)