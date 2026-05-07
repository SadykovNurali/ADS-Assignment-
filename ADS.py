graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C', 'E', 'G'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A'],
    'E': ['G', 'F', 'B'],
    'F': ['G', 'E'],
    'G': ['F', 'B']
}

# DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# BFS
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

print("DFS:", dfs(graph, 'A'))
print("BFS:", bfs(graph, 'A'))