from collections import deque

                    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(land):
    depth = len(land)
    x_len = len(land[0])
    
    max = 0
    for x in range(x_len):
        visited = set()
        for y in range(depth):
            dfs(land,visited,x,y) 
        
        if max < len(visited):
            max = len(visited)
    return max


                    
def dfs(graph,visited,x,y):
    
    # 현재 위치가 범위를 벗어나거나 이미 방문한 경우 함수 종료
    if x < 0 or y < 0 or x >= len(graph[0]) or y >= len(graph) or (y, x) in visited:
        return
    
    if (y,x) in visited:
        return
    
    # 현재 위치가 1이면, 4방향 탐색
    if graph[y][x] == 1:
        visited.add((y, x))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph,visited,nx,ny)
    elif graph[y][x] == 0:
        return