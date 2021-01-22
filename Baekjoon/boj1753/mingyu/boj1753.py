"""
Baekjoon 1753. 최단경로
url: https://www.acmicpc.net/problem/1753
writer: Mingyu
Language: Python3
Date: 2021.01.18
Status: , Runtime:  ms, Memory Usage:  KB
"""

#  일반 input이 효율적이지 않기 때문에 알고리즘 문제에서는 sys를 쓰는 경우도 많다.
import sys
from heapq import heappush, heappop
from collections import defaultdict

# 정점의 개수, 간선의 개수, 시작값을 입력
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 무한을 최대값으로 표현
INF = sys.maxsize

# 가중치 테이블을 노드 개수 + 1의 크기만큼 초기화. 노드 번호가 1부터 시작하고 이를 키 값으로 쓸 것이기 때문이다.
dp = [INF] * (V + 1)

# 우선순위 큐
heap = []

# 그래프를 그릴 배열. 인자를 list로 초기화한 dict을 사용한다.
graph = defaultdict(list)

# 다익스트라 알고리즘
def Dijkstra(start):
    # 시작 지점은 거리가 0이다
    dp[start] = 0

    # 우선순위 큐에 거리와 노드를 넣음
    heappush(heap, (0, start))

    # 우선순위 큐가 빌 때까지
    while heap:

        # 현재까지 지나온 거리와 해당 노드를 가져온다.
        cur_w, cur_n = heappop(heap)

        # dp[node]는 해당 노드까지의 최단 거리를 저장해둔 배열이다
        # 이 거리가 방금 받아온 거리보다 작다면 굳이 검사할 필요 없이 다음 단계로 넘어가도 된다.
        if dp[cur_n] < cur_w:
            continue

        # 방금 가져온 노드에 인접한 노드까지의 거리(가중치)와 인접한 노드의 이름을 가져온다
        for adj_w, adj_n in graph[cur_n]:

            # 현재까지 지나온 거리와 인접한 노드까지의 거리의 함
            distance = cur_w + adj_w

            # 이 거리가 해당 노드까지의 최단거리(dp[adj_n])보다 작다면
            if distance < dp[adj_n]:

                # 해당 노드까지의 거리를 distance로 업데이트한 후 우선순위 큐에 넣는다.
                dp[adj_n] = distance
                heappush(heap, (distance, adj_n))


# 간선의 가중치 입력
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))

# 다익스트라 알고리즘을 활용하여 dp테이블을 완성한 후
Dijkstra(K)

# dp[i]가 INF라면 INF를 출력, 아니라면 해당 숫자를 출력
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])



''' 주석 없는 코드
import sys
from heapq import heappush, heappop

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

INF = sys.maxsize
dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V + 1)]


def Dijkstra(start):
    dp[start] = 0
    heappush(heap, (0, start))

    while heap:
        cur_w, cur_n = heappop(heap)

        if dp[cur_n] < cur_w:
            continue

        for adj_w, adj_n in graph[cur_n]:
            distance = cur_w + adj_w

            if distance < dp[adj_n]:
                dp[adj_n] = distance
                heappush(heap, (distance, adj_n))


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))

Dijkstra(K)

for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])

'''