#Kavana Manvi Krishnamurthy
import sys
from collections import deque

def DFS(v):
    marked[v] = True
    previsit.append(v)
    
    for w in range(n):
        if A[v][w] == 1 and not marked[w]:
            parent[w] = v
            DFS(w)
    postvisit.append(v)

def print_matrix(A):
    for row in A:
        print(row)

def print_list(lst):
    print(' '.join(map(str, lst)))

print("Kavana Manvi Krishnamurthy")

if len(sys.argv) != 2:
    print("Usage: python DFSTest.py <file_path>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

with open(file_path, "r") as file:
    lines = file.readlines()

n = int(lines.pop(0).strip())
A = [[0] * n for _ in range(n)]
m = int(lines.pop(0).strip())

for line in lines:
    u, v = map(int, line.split())
    A[u][v] = 1
    A[v][u] = 1  # Because the graph is undirected

# Create a previsit deque
previsit = deque()

# Create a postvisit deque
postvisit = deque()

marked = [False] * n
parent = [-1] * n

# Call DFS starting from vertex 1
DFS(1)

print("Previsit order:")
print_list(previsit)

print("Postvisit order:")
print_list(postvisit)
