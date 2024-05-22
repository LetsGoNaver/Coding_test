def solution(rows, columns, queries):
    answer = []
    graph = [[j + i * columns + 1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        first = graph[x1][y1]
        min_val = first

        # Move top row
        for i in range(x1, x2):
            graph[i][y1] = graph[i + 1][y1]
            min_val = min(min_val, graph[i][y1])

        # Move left column
        for i in range(y1, y2):
            graph[x2][i] = graph[x2][i + 1]
            min_val = min(min_val, graph[x2][i])

        # Move bottom row
        for i in range(x2, x1, -1):
            graph[i][y2] = graph[i - 1][y2]
            min_val = min(min_val, graph[i][y2])

        # Move right column
        for i in range(y2, y1, -1):
            graph[x1][i] = graph[x1][i - 1]
            min_val = min(min_val, graph[x1][i])

        # Restore first value
        graph[x1][y1 + 1] = first

        answer.append(min_val)

    return answer
