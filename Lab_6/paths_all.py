class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_edge(self, vertex):
        node = Node(vertex)
        node.next = self.head
        self.head = node

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    # print(path)
    if start == end:
        return [path]
    if not graph.get(start):
        return []
    paths = []
    current_node = graph[start].head
    # print(f'current node: {current_node} for path: {path} where the accumalted final paths are : {paths}')
    while current_node:
        if current_node.value not in path:
            new_paths = find_all_paths(graph, current_node.value, end, path)
            for p in new_paths:
                paths.append(p)
        current_node = current_node.next
    return paths

def print_all_paths(graph, start, end):
    paths = find_all_paths(graph, start, end)
    if not paths:
        print(f"No path found between {start} and {end}.")
    else:
        print(f"All paths between {start} and {end}:")
        for path in paths:
            print(" -> ".join(map(str, path)))

# Example usage:
graph = {
    'A': LinkedList(),
    'B': LinkedList(),
    'C': LinkedList(),
    'D': LinkedList(),
    'E': LinkedList(),
    'F': LinkedList(),
    'M': LinkedList(),
}

graph['A'].add_edge('B')
graph['A'].add_edge('C')
graph['A'].add_edge('M')
graph['B'].add_edge('D')
graph['B'].add_edge('E')
graph['B'].add_edge('M')
graph['C'].add_edge('F')
graph['C'].add_edge('M')
graph['D'].add_edge('B')
graph['E'].add_edge('F')
graph['F'].add_edge('E')
graph['F'].add_edge('C')
graph['M'].add_edge('A')
graph['M'].add_edge('B')
graph['M'].add_edge('C')
graph['M'].add_edge('F')

start = input('Please enter the starting point for the graph: ')
end = input('Please enter the ending point for the graph: ')
print_all_paths(graph, start, end)
