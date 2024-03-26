import bisect

def solution(edges):
    # 생성 정점,  도넛 , 막대 , 8자
    answer = []
    created_node = 0
    donut = 0
    stick = 0
    eight = 0
    
    first = []
    second = []
    
    for i in edges:
        first.append(i[0])
        second.append(i[1])
    
    def intersection(nums1,nums2):
        result = []
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2,n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                continue
            else:
                result.append(n1)
        
        count = 0
        for r in result:
            if result.count(r) != 1 :
                result = [r]
        return result
    
    
    created_node = intersection(first,second).pop()
    print(created_node)

    # 생성된 정점을 위에서 구했음
    
    connected_nodes = [] # 생성된 정점에 연결된 노드
    for i in edges:
        if i[0] == created_node:
            connected_nodes.append(i[1])
      
    dic = dict()
    
    for i in connected_nodes :
        dic[i] = [] 
    
    graph = {}
    
    for e in edges:
        s , ed = e[0] , e[1]
        if s == created_node:
            continue
        else:
            if s not in graph.keys():  
                graph[s] = [ed]
            else:
                graph[s].append(ed)
    
    from collections import deque
    
    def bfs(node) :
        visited = [node]
        queue = deque([node])
        arrows = 0
        while queue :
            q = queue.popleft()
            try:
                for g in graph[q]:
                    arrows += 1
                    if g not in visited:
                        visited.append(g)
                        queue.append(g)
            except KeyError:
                        return[[1],0]
        return [visited,arrows] # 앞 -> 노드 번호들 , 뒤 -> 화살표들
    
    

    # 문제1 에서 3과 같은 경우는 나가는 방향이 없기 때문에 할 수 있는게 없음! 문제임!
    for key in dic.keys() :
        dic[key] = bfs(key)
    
    for key in dic.keys():
        node_count = len(dic[key][0])
        arrows = dic[key][1]
        
        if node_count == arrows :
            donut += 1
        elif node_count - 1 == arrows :
            stick += 1
        elif node_count + 1 == arrows :
            eight += 1
        else:
            continue
        

    
    answer.append(created_node)
    answer.append(donut)
    answer.append(stick)
    answer.append(eight)
    return answer