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

def print_equidistant_nodes(graph, root):
    if root not in graph:
        print(f"Node {root} not found in the graph.")
        return
    
    queue = [(root, 0)]  # Tuple containing current node and its distance from the root
    result = {}

    while queue:
        current_node, current_distance = queue.pop(0)

        if current_node in graph:
            current_neighbor = graph[current_node].head
            while current_neighbor:
                neighbor_value = current_neighbor.value
                queue.append((neighbor_value, current_distance + 1))

                if current_distance + 1 not in result:
                    result[current_distance + 1] = [neighbor_value]
                else:
                    result[current_distance + 1].append(neighbor_value)

                current_neighbor = current_neighbor.next

    for distance, nodes in result.items():
        print(f"Nodes at distance {distance} from root {root}: {', '.join(map(str, nodes))}")


graph = {}


# while True:
#     node = input('Add a New node to the graph')
#     check = 'Y'
#     while check == 'Y':
#         edge = input('Add a Edge to Node {node}: ')
#         add_edge(graph, node, edge)
#         check = input('Want to Add More  Edges? (y/n): ').upper()
#     cont = input('Want to Add More Nodes? (y/n): ').upper()
#     if (cont == 'N'):
#         break       
        
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'D')
add_edge(graph, 'B', 'E')
add_edge(graph, 'C', 'F')
add_edge(graph, 'C', 'G')
add_edge(graph, 'E', 'M')

print_equidistant_nodes(graph, 'A')
