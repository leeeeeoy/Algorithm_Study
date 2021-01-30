"""
Baekjoon 1260. DFS와 BFS
url: https://www.acmicpc.net/problem/1260
writer: Harim Kang
Language: Python3
Date: 2021.01.08
Status: Success, Runtime: 640 ms, Memory Usage: 34252 KB
"""

from typing import DefaultDict

# input을 받는 코드 : N, M, V
N, M, V = map(int, input().split())

# graph는 연결리스트를 작성
graph = DefaultDict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬된 상태에서의 탐색을 문제가 원하고 있다.
for i in graph.keys():
    graph[i].sort()


def search(s, method):
    # s는 시작 노드를 의미한다.
    # method는 dfs와 bfs 두개의 방식이며, graph 순서와 pop위치를 다르게 주었다.
    visited = [0] * N
    temp = [s]
    path = []

    while temp:
        if method == "dfs":
            current = temp.pop()
            temp_graph = graph[current][::-1]
        else:
            current = temp.pop(0)
            temp_graph = graph[current]

        if visited[current - 1] == 0:
            visited[current - 1] = 1
            path.append(current)
        for node in temp_graph:
            if visited[node - 1] == 0:
                temp.append(node)

    for i in path:
        print(i, end=" ")
    print()


search(V, method="dfs")
search(V, method="bfs")
