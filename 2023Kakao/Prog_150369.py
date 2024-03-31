def solution(cap, n, d, p):
    answer, dcap, pcap = 0, 0, 0

    for i in range(n - 1, -1, -1):
        if d[i] != 0 or p[i] != 0:
            cnt = 0
            while dcap < d[i] or pcap < p[i]:
                cnt += 1
                dcap += cap
                pcap += cap
            dcap -= d[i]
            pcap -= p[i]
            answer += ((i + 1) * cnt * 2)

    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))