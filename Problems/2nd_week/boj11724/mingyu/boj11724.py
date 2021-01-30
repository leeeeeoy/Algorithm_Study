"""
Baekjoon 11724. 연결 요소의 개수
url: https://www.acmicpc.net/problem/11724
writer: Mingyu
Language: Python3
Date: 2021.01.20
Status: , Runtime:  ms, Memory Usage:  KB
"""
# 입력을 위한 외부 모듈
import sys

# 파이썬에서 재귀의 깊이는 보통 1000으로 설정되어 있다. 런타임 에러가 나지 않게 10000으로 조정해주자.
sys.setrecursionlimit(10000)

# dfs를 재귀로 구현.
# node는 현재 검사의 시작점이 되는 노드이다.
# 안에서 활용하는 visited와 graph 배열은 전역변수로 선언되어 있기에 활용이 가능하다.
def dfs(node):
    # 검사를 실행한 노드이므로 값을 참(True)으로 설정
    visited[node] = True

    # 해당 노드에 인접한 노드들을 돌면서
    for i in graph[node]:
        # 아직 방문하지 못한 노드를 발견했다면
         if not visited[i]:
             # dfs에 집어넣는다.
             dfs(i)

# 정점의 개수와 간선의 개수 입력
n, m = map(int, sys.stdin.readline().split())

# 노드가 방문했는지 확인할 배열. 방문했다면 True, 방문하지 않았다면 False를 사용할 것이기 때문에 처음에는 전부 방문하지 않음(False)로 설정
# n + 1인 이유는 노드 번호가 1부터 시작하기 때문이다. 0번 노드는 활용하지 않음
visited = [False] * (n + 1)

# 그래프를 그리기 위한 배열. 각 노드가 어떤 노드와 연결되어 있는지 그리기 위해 2중배열을 사용한다. ex) graph[1] = [x, y] 등
graph = [[] for _ in range(n + 1)]

# 무방향(양방향)이므로 u노드와 v노드가 서로를 가리키도록 해준다.
for _ in range(m):
    u ,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결된 노드 집합(연결 요소)의 개수를 저장할 변수
cnt = 0

# 1부터 n+1인 이유는 아까 말했듯 노드 번호가 1부터 시작하기 때문이다.
for i in range(1, n + 1):
    # 해당 노드가 아직 방문하지 않은 노드라면, 즉 방문하지 않은 집합이라면
    if not visited[i]:
        # dfs를 실행한 후 집합의 개수를 추가한다.
        dfs(i)
        cnt += 1

# 연결 요소의 개수 출력
print(cnt)




''' 주석 없는 코드
import sys
sys.setrecursionlimit(10000)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
         if not visited[i]:
             dfs(i)

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u ,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
        
print(cnt)

'''