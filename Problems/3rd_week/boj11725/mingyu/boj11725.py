"""
Baekjoon 11725. 트리의 부모 찾기
url: https://www.acmicpc.net/problem/11725
writer: Mingyu
Language: Python3
Date: 2021.01.26
Status: , Runtime:  ms, Memory Usage:  KB
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
# 그래프 생성, (N+1)인 이유는 노드 번호가 1부터 시작하기 때문이다. 인덱스 번호는 0부터 시작하기 때문에 +1을 해준다.
graph = [[] for _ in range(N + 1)]
# 연결된 두 정점이라고 하였으므로 양방향 간선으로 판단한다. 서로 이어주자.
for _ in range(N - 1):
    a, b = (map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모 노드 번호를 저장할 배열.
parent = [0] * (N + 1)
# 트리의 루트를 1로 정한다.
parent[1] = 1

# BFS를 사용하기 위해 덱 생성. 루트 노드인 1부터 시작할 것이기 때문에 바로 넣어준다.
# 리스트 형태로 넣어줘야 하기 때문에 [1]로 넣는 것이다.
dq = deque([1])

# BFS
while dq:
    node = dq.popleft()
    # 해당 노드와 연결된 노드들을 돌면서
    for child in graph[node]:
        # 확인중인 노드에 부모가 설정되어 있지 않다면
        if not parent[child]:
            # 현재 노드를 해당 노드의 부모로 설정
            parent[child] = node
            # 해당 노드를 dq에 넣어준다.
            dq.append(child)

# 부모 노드 번호를 2번 노드부터 순서대로 출력할 것이다.
for parent in parent[2:]:
    print(parent)



''' 주석 없는 코드
import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = (map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
parent[1] = 1

dq = deque([1])

while dq:
    node = dq.popleft()
    for child in graph[node]:
        if not parent[child]:
            parent[child] = node
            dq.append(child)

for parent in parent[2:]:
    print(parent)
'''