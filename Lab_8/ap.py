class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]
        self.time = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def APUtil(self, u, visited, disc, low, parent, ap):
        children = 0
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.adj[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self.APUtil(v, visited, disc, low, parent, ap)
                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def AP(self):
        visited = [False] * self.V
        disc = [float("inf")] * self.V
        low = [float("inf")] * self.V
        parent = [-1] * self.V
        ap = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.APUtil(i, visited, disc, low, parent, ap)

        print("Articulation Points in the Graph:")
        for i in range(self.V):
            if ap[i]:
                print(i, end=" ")


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    print("Articulation Points in the given graph:")
    g.AP()
