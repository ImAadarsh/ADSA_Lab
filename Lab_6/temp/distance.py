class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = LinkedList()
    graph[u].add_node(v)

def print_equidistant_nodes(graph, root, distance):
    if root not in graph:
        print(f"Node {root} not found in the graph.")
        return
    
    queue = [(root, 0)]  # Tuple containing current node and its distance from the root

    while queue:
        current_node, current_distance = queue.pop(0)

        if current_distance == distance:
            print(f"Node: {current_node}, Distance: {current_distance}")
            

        if current_node in graph:
            current_neighbor = graph[current_node].head
            while current_neighbor:
                queue.append((current_neighbor.value, current_distance + 1))
                current_neighbor = current_neighbor.next

# Example usage:
graph = {}

add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'D')
add_edge(graph, 'B', 'E')
add_edge(graph, 'C', 'F')
add_edge(graph, 'C', 'G')

print("Equidistant nodes from root 'A' with distance 2:")
print_equidistant_nodes(graph, 'B', 1)











print_equidistant_nodes(graph, 'A')