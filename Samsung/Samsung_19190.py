T = int(input())

for test_case in range(1, T + 1):
    n,m1 = map(int,input().split())
    must_go = []
    for _ in range(m1):
        p = list(map(int, input().split()))
        must_go.append(p)
    m2  = int(input())
    normal_path = []
    for _ in range(m2):
        p = list(map(int, input().split()))
        normal_path.append(p)
    print(must_go)
    print(normal_path)

    # 1에서 출발하고 다시 1로 와야해
    dic = dict()
    
    start = 1
    start_d = 0
    while start < n:
        for m in must_go:
            if m[0] == start:
               start = m[1]
               start_d += m[2]
        
        for n in normal_path:
            if n[0] == start:
                start = n[1]
                start_d += n[2]
                