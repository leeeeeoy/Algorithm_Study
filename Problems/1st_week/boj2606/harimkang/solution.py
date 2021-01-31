"""
Baekjoon 2606. 바이러스
url: https://www.acmicpc.net/problem/2606
writer: Harim Kang
Language: Python3
Date: 2021.01.09
Status: Success, Runtime: 148 ms, Memory Usage: 33888 KB
"""

from typing import DefaultDict


N = int(input())

graph = DefaultDict(list)

for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N)]


def dfs(s):
    # s는 시작 노드를 의미한다. 스택을 사용하여 구현
    stack = [s]
    answer = 0

    while stack:
        # stack이 빌 때까지 반복한다.
        current = stack.pop()
        if visited[current - 1] == 0:
            visited[current - 1] = 1
            answer += 1
        for i in graph[current]:
            if visited[i - 1] == 0:
                # 현재 위치한 노드를 기준으로 연결되어 있고,
                # 방문한 적이 없는 노드만 스택에 담는다.
                stack.append(i)
    return answer - 1


print(dfs(1))