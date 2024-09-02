#Kavana Manvi Krishnamurthy
import sys
from collections import deque

def initSSSP(s):
    dist[s]=0
    pred[s]= None
    for  v in vertices:
        if v!=s:
            dist[v]=float('inf')
            pred[v]=None
    

def BFS(s):
    answer=[]
    initSSSP(s)
    queue.append(s)
    queue.append(-1)
    while queue:
        u = queue.popleft()
        answer.append(u)
        if u == -1 and queue:
            queue.append(-1)
        else:
            for v in range(0,n):
                if A[u][v] == 1 and dist[v]>dist[u]+1:
                    dist[v]=dist[u]+1
                    pred[v]=u
                    queue.append(v)
    for i in range(0,len(answer)):
        if answer[i] == -1:
            answer[i] = '|'

    print(*answer)
       
    


print("Kavana Manvi Krishnamurthy")

if len(sys.argv) != 2:
    print("Usage: python DFSTest.py <file_path>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

with open(file_path, "r") as file:
    lines = file.readlines()

n = int(lines.pop(0).strip())
m=  int(lines.pop(0).strip())
A = [[0] * n for _ in range(n)]

for line in lines:
    u, v = map(int, line.split())
    A[u][v] = 1

dist = [0] * n
pred = [0] * n
vertices = [i for i in range(0,n)]
queue = deque()
BFS(0)