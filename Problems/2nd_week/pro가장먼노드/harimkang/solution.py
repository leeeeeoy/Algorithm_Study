"""
Programmers 49189. 가장 먼 노드
url: https://programmers.co.kr/learn/courses/30/lessons/49189
writer: Harim Kang
Language: Python3
Date: 2021.01.29
Status: Success
정확성: 100.0
합계: 100.0 / 100.0
"""

import collections


def solution(n, vertex):
    visited = [0 for _ in range(n)]

    # 관계 graph 형성
    graph = collections.defaultdict(list)
    for v, u in vertex:
        graph[v].append(u)
        graph[u].append(v)

    levels = collections.defaultdict(int)

    # dfs방식으로, 노드를 하나씩 방문하면서 방문 여부를 체크하는 함수
    def bfs(s):
        # s는 시작 노드를 의미한다. 스택을 사용하여 구현
        stack = [[0, s]]
        max_level = 0

        while stack:
            # stack이 빌 때까지 반복한다.
            level, current = stack.pop(0)
            if visited[current - 1] == 0:
                visited[current - 1] = 1
            for next in graph[current]:
                if visited[next - 1] == 0:
                    # 현재 위치한 노드를 기준으로 연결되어 있고,
                    # 방문한 적이 없는 노드만 스택에 담는다.
                    if level + 1 > max_level:
                        max_level = level + 1
                    stack.append([level + 1, next])
                    visited[next - 1] = 1
                    levels[level + 1] += 1
        return max_level

    deep = bfs(1)

    return levels[deep]


if __name__ == "__main__":
    inputs = [
        [6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]],
    ]
    expected = [3]
    resp = []
    for n, vertex in inputs:
        ans = solution(n, vertex)
        resp.append(ans)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)