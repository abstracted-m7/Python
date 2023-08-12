# 1. write a python program to evalute the prefix expression "+9*26"
def evaluate_prefix_expression(expression):
    stack = []
    operators = set(["+", "-", "*", "/"])

    # Iterate through the expression in reverse order
    for i in range(len(expression) - 1, -1, -1):
        if expression[i].isdigit():
            stack.append(int(expression[i]))
        elif expression[i] in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = perform_operation(expression[i], operand1, operand2)
            stack.append(result)

    return stack.pop()


def perform_operation(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


expression = "+9*26"
result = evaluate_prefix_expression(expression)
print("The result : ", result)