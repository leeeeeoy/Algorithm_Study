"""
programmers 43164. 여행경로
url: https://programmers.co.kr/learn/courses/30/lessons/43164
writer: Harim Kang
Language: Python3
Date: 2021.02.21
Status: Success, Runtime: 28 ms, Memory Usage: 14.6 MB
"""
from collections import defaultdict


def solution(tickets):
    route = defaultdict(list)

    # 약간 변형된 DFS 사용
    def dfs(start):
        path = []
        while start:
            recent = start[-1]
            if recent not in route or len(route[recent]) == 0:
                path.append(start.pop())
            else:
                start.append(route[recent].pop(0))
        return path[::-1]

    for dep, arr in tickets:
        route[dep].append(arr)

    stack = ["ICN"]
    for t in route:
        route[t].sort()

    return dfs(stack)


if __name__ == "__main__":
    inputs = [
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
        [
            ["ICN", "SFO"],
            ["ICN", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "ICN"],
            ["ATL", "SFO"],
        ],
    ]
    expected = [
        ["ICN", "JFK", "HND", "IAD"],
        ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"],
    ]
    resp = []
    for input in inputs:
        resp.append(solution(input))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)