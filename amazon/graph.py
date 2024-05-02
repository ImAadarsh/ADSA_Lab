class Graph:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.list = []
    def insert (self, where):
        temp = Graph()
        if where in list:
            choice = "yes"
            while choice == "yes":
                print("Do you want to add more nodes?")
                choice = input().lower()
                if choice != "no":
                    node_value = int(input("Enter the value of new node :"))
                    temp.data = node_value
                    temp.next = self.list[where].next
                    self.list[where].next=temp
                else:
                    break
        elif where < 0 or where >= len(self.list):
            print("Invalid position!")
        else:
            print("Position out of range.")
            




                
        
        
        