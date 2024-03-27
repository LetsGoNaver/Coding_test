from collections import deque

def solution(n, wires):
    answer = -1
    minimum = 999
    
    for i in range(len(wires)):
        part = wires[:i]
        part_two = wires[i+1:] 
        starting = wires[i] # 끊긴 부분을 알려줌
        
        for i in part_two:
            part.append(i)
            
        graph = dict()
        
        for i in range(1,n+1):
            graph[i] = []
            
        for p in part:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
        
        one = len(bfs(graph,starting[0]))
        two = len(bfs(graph,starting[1]))

        if abs(one-two) < minimum:
            minimum = abs(one-two)

    answer = minimum
    return answer


def bfs(graph,node):
    q = deque([node])
    visited = [node]
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited