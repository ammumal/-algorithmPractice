from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nodes = [[] for i in range(n)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    nodes[x-1].append([w, y-1])
    nodes[y-1].append([w, x-1])

def bfs(start, mode):
    q = deque()
    q.append(start)
    visited = [-1 for i in range(n)]
    visited[start] = 0
    
    while q:
        x = q.popleft()
        for i, j in nodes[x]:
            if visited[j] == -1:
                visited[j] = visited[x] + i
                q.append(j)
    if mode == 1:
        return visited.index(max(visited))
    else:
        return max(visited)

print(bfs(bfs(0, 1), 2))
