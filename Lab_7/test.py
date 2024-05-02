def assign_weights(n):
    graph = {i: [] for i in range(1, n + 1)}

    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if u != v:
                weight_uv = 1 if u % v == 0 or v % u == 0 else n + 1
                graph[u].append((v, weight_uv))
    return graph


n = 4
weighted_graph = assign_weights(n)

# In this code find the shortest path between two nodes in this program

# Display the weighted graph
for node, neighbors in weighted_graph.items():
    print(f"Node {node}: {neighbors}")

def dijkstra(graph, start, end):
    distance = {node: float('inf') for node in graph}
    # print(distance)
    distance[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda x: distance[x])
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            if distance[current_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_node] + weight
        print(distance) 
        # print(visited)

    return distance[end]

# Example usage:
start_node = 2
end_node = 3

shortest_distance = dijkstra(weighted_graph, start_node, end_node)
print(f"The shortest distance between Node {start_node} and Node {end_node} is: {shortest_distance}")

