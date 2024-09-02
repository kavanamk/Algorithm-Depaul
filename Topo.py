from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, postvisit_stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self._dfs(i, visited, postvisit_stack)

        # Push current vertex to postvisit_stack which stores result
        postvisit_stack.append(v)

    def topo_sort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        postvisit_stack = []

        # Call the recursive helper function to store Topological Sort
        # starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, postvisit_stack)

        # Print contents of the stack
        while postvisit_stack:
            print(postvisit_stack.pop())

# Example usage:
g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,5)
g.add_edge(1,4)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(3, 6)
g.add_edge(5,2)
g.add_edge(6,0)
g.add_edge(6,4)

print("Topological Sort of the given graph:")
g.topo_sort()
