from collections import deque
def solution(n, computers):
    answer = 0
    graph = dict()
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1:
                graph[i].append(j)
    
    def bfs(node):
        q = deque([node])
        visited = [node]
        
        while q:
            v = q.popleft()
            for p in graph[v]:
                if p not in visited:
                    visited.append(p)
                    q.append(p)
        return visited
    
    will_visit = deque(range(n))
    
    while will_visit:
        p = will_visit.popleft()
        checked = bfs(p)
        answer += 1
        for c in checked:
            if c == p:
                continue
            else:
                will_visit.remove(c)

    return answer