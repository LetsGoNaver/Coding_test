from collections import deque

def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

def dfs(graph,start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.append(graph[v])

def bfs(graph,start_node):
    visited = [start_node]
    queue = deque([start_node])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
