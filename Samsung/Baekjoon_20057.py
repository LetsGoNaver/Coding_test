n = int(input())
graph = []
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)
#왼쪽 : 두번째 -1
#아래 : 첫번째 +1
#오른쪽 : 두번째 +1
#위 : 첫번째 -1


def solution(n,graph):
    answer = 0
    m = int((n-1)/2)
    start = [m,m]

    d = ["left","right","up","down"]
    
    
    moving = [
        [(-2,0),(-1,-1), (-1,0), (-1,1),(0,-2), (1,-1),(1,0),(1,1),(2,0),(0,-1)],
     [(0,-2),(1,-1), (0,-1), (-1,-1),(2,0), (1,1),(0,1),(-1,1),(0,2),(1,0)],
     [(2,0),(1,1), (1,0), (1,-1),(0,2), (-1,1),(-1,0),(-1,-1),(-2,0),(0,1)],
     [(0,2),(-1,1), (0,1), (1,1),(-2,0), (-1,-1),(0,-1),(1,-1),(0,-2),(-1,0)]
     ]
    percentage =[0.01,0.01,0.02,0.02,0.07,0.07,0.1,0.1,0.05,0.65]

    def is_out(x,y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return True
        return False

    def blow(point,direction):
        depth = point[0]
        x = point[1]
        blown = 0
        if graph[depth,x] != 0:
            if direction == "left":
                inx = d.index(direction)
                for i in range(10):
                    depth += moving[inx][0]
                    x += moving[inx][1]
                
        return blown

    for i in range(1,n):
        if i%2 != 0:
            start[1] -= i
            arrow = "left"
            blow(start,arrow)
            start[0] += i
            arrow = "down"
            blow(start,arrow)
        else:
            start[1] += i
            arrow = "right"
            blow(start,arrow)
            start[0] -= i
            arrow = "up"
            blow(start,arrow)

    start[1] -= n-1
    arrow = "left"
    blow(start,arrow)
    return answer