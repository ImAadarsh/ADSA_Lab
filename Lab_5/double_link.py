class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            
    def search(self, data):
        pos = 0
        current = self.head
        while current:
            if current.data == data:
                return pos
            current = current.next
            pos += 1
        return -1

    def delete(self, data):
            if not self.head:
                return
            if self.head.data == data:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    if current.next:
                        current.next.prev = current
                    return
                current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def displayReserve(self):
        elements = []
        current = self.head
        while current.next:
            current = current.next
        previous = current
        while previous:
            elements.append(previous.data)
            previous = previous.prev
        return elements


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Reverse Display")
        print("5. Search Element")
        print("6. Quit")
        option = int(input("Enter your option: "))
        if option == 1:
            data = int(input("Enter the data to insert: "))
            linked_list.insert(data)
        elif option == 2:
            data = int(input("Enter the data to delete: "))
            linked_list.delete(data)
        elif option == 3:
            print("The linked list is: ", linked_list.display())
        elif option == 4:
            print("The Reverse linked list is: ", linked_list.displayReserve())
        elif option == 5:
            data = int(input("Enter the data to search for: "))
            result = linked_list.search(data)
            if result != -1:
                print("Element found at position: ", result)
            else:
                print("Element not found")
        elif option == 6:
            break
        else:
            print("Invalid option, please try again.")
            
            