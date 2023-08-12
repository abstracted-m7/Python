# Write a Python program to evaluate the postfix expression “2 3 +”
def evaluate_postfix_expression(expression):
    stack = []
    for i in expression.split():
        if i.isdigit():
            stack.append(int(i))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(i, operand1, operand2)
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


expression = "2 3 +"
result = evaluate_postfix_expression(expression)
print("The result :", result)
