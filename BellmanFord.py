from collections import deque
import heapq

# Initialize the single source shortest path
def initSSSP(s, vertices, dist, pred):
    dist[s] = 0
    pred[s] = None
    for v in vertices:
        if v != s:
            dist[v] = float('inf')
            pred[v] = None

# Relax the edge (u -> v) if the new distance is shorter
def RelaxEdge(u, v, weight, dist, pred):
    dist[v] = dist[u] + weight
    pred[v] = u

# Bellman-Ford Algorithm
def BellmanFord(s, n, matrix):
    vertices = range(n)
    dist = {}
    pred = {}
    initSSSP(s, vertices, dist, pred)
    
    # Convert adjacency matrix to edge list
    edgeList = createEdgeList(matrix)
    
    # Relax all edges (n-1) times
    for i in range(n - 1):
        for edge in edgeList:
            u, v, weight = edge
            if dist[u] + weight < dist[v]:
                RelaxEdge(u, v, weight, dist, pred)
        print(f"Iteration {i+1}:")
        print("Distances:", dist)
        print("Predecessors:", pred)
        print()
    
    # Check for negative-weight cycles
    for edge in edgeList:
        u, v, weight = edge
        if dist[u] + weight < dist[v]:
            return False  # Negative-weight cycle found
    return dist, pred  # No negative cycle, return distances and predecessors

# Function to create an edge list from the adjacency matrix
def createEdgeList(matrix):
    edgeList = []
    for u in range(len(matrix)):
        for v in range(len(matrix[u])):
            if matrix[u][v] != float('inf'):  # If there's an edge from u to v
                edgeList.append((u, v, matrix[u][v]))
    return edgeList

# Adjacency matrix representation of the graph
n = 5  # Number of vertices
matrix = [
    [float('inf'), 6, 7, float('inf'), float('inf')],  # Edges from vertex 0
    [float('inf'), float('inf'), 8, 5, -4],            # Edges from vertex 1
    [float('inf'), float('inf'), float('inf'), -3, 9],  # Edges from vertex 2
    [float('inf'), -2, float('inf'), float('inf'), float('inf')],  # Edges from vertex 3
    [float('inf'), float('inf'), float('inf'), 7, float('inf')]    # Edges from vertex 4
]

# Run the Bellman-Ford algorithm starting from vertex 0
result = BellmanFord(0, n, matrix)
if result is False:
    print("Negative-weight cycle detected!")
else:
    dist, pred = result
    print("Final Distances:", dist)
    print("Predecessors:", pred)
