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

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek from an empty stack.")
            return None
        return self.top.data

    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements


if __name__ == "__main__":
    stack = Stack()
    
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Quit")
        option = int(input("Enter your option: "))
        
        if option == 1:
            data = int(input("Enter the data to push: "))
            stack.push(data)
        elif option == 2:
            popped_data = stack.pop()
            if popped_data is not None:
                print("Popped element: ", popped_data)
        elif option == 3:
            peeked_data = stack.peek()
            if peeked_data is not None:
                print("Top element: ", peeked_data)
        elif option == 4:
            print("Stack elements: ", stack.display())
        elif option == 5:
            break
        else:
            print("Invalid option, please try again.")
