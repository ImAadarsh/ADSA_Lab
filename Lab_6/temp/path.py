def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.get(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
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
    'A': ['B', 'C', 'M'],
    'B': ['D', 'E', 'M'],
    'C': ['F', 'M'],
    'D': ['B'],
    'E': ['F'],
    'F': ['E', 'C'],
    'M': ['A', 'B', 'C', 'F'],
}

print_all_paths(graph, 'D', 'E')

