n = int(input())
graph = []
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

def solution(n,graph):
    def printing():
        print("----------------")
        for i in graph:
            print(i)
        print("----------------")
    answer = 0
    m = int((n-1)/2)
    start = [m,m]

    d = ["left","right","up","down"]
    
    
    moving = [
        [(-1,1),(1,1),(2,0),(-2,0),(-1,0),(1,0),(-1,-1),(1,-1),(0,-2),(0,-1)],
        [(-1,-1),(1,-1),(2,0),(-2,0),(-1,0),(1,0),(-1,1),(1,1),(0,2),(0,1)],
        [(1,-1),(1,1),(0,-1),(0,1),(2,0),(-2,0),(-1,-1),(-1,1),(-2,0),(-1,0)],
        [(-1,-1),(-1,1),(0,-1),(0,1),(2,0),(-2,0),(1,-1),(1,1),(2,0),(1,0)]
     ]
    percentage =[0.01,0.01,0.02,0.02,0.07,0.07,0.1,0.1,0.05,1] # 마지막에서는 전체에서 - 날라간양

    def is_out(x,y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return True
        return False

    def blow(point,direction):
        depth = point[0]
        x = point[1]
        blown = 0
        if graph[depth][x] != 0:
            inx = d.index(direction)
            moved_sand = 0
            for i in range(10):
                td = point[0]
                tx = point[1]
                sand = int(graph[td][tx]*percentage[i])
                moved_sand += sand
                td += moving[inx][i][0]
                tx += moving[inx][i][1]
                if is_out(td,tx):
                    blown += sand
                else:
                    graph[td][tx] += sand
                
                if i == 9:
                    td = point[0]
                    tx = point[1]
                    sand = graph[td][tx] - moved_sand
                    td += moving[inx][i][0]
                    tx += moving[inx][i][1]
                    if is_out(td,tx):
                        blown += sand
                    else:
                        graph[td][tx] += sand

            graph[depth][x] = 0
                
        return blown

    for i in range(1,n):
        if i%2 != 0:
            for _ in range(i):
                start[1] -= 1
                arrow = "left"
                answer += blow(start,arrow)
                printing()
            for _ in range(i):
                start[0] += 1
                arrow = "down"
                answer += blow(start,arrow)
                printing()
        else:
            for _ in range(i):
                start[1] += 1
                arrow = "right"
                answer += blow(start,arrow)
                printing()
            for _ in range(i):
                start[0] -= 1
                arrow = "up"
                answer += blow(start,arrow)
                printing()

    for _ in range(n-1):
        start[1] -= 1
        arrow = "left"
        answer += blow(start,arrow)
        printing()
    return answer

print("answer is",solution(n,graph))


