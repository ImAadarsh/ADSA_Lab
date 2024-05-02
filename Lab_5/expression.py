class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop from an empty stack.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                if operand2 == 0:
                    print("Error: Division by zero.")
                    return None
                result = operand1 / operand2

            stack.push(result)

    if stack.is_empty():
        print("Error: Invalid postfix expression.")
        return None

    return stack.pop()

if __name__ == "__main__":
    postfix_expression = input("Enter a postfix expression: ")
    result = evaluate_postfix(postfix_expression)

    if result is not None:
        print("Result of the postfix expression is:", result)
