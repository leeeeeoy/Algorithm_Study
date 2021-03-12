"""
Baekjoon 15900. 나무 탈출
url: https://www.acmicpc.net/problem/15900
writer: Mingyu
Language: Python3
Date: 2021.01.27
Status: , Runtime:  ms, Memory Usage:  KB
"""
'''
1. 리프 노드까지의 depth의 합이 홀수면 성원이가 이긴다.
'''

# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
# 입력 및 그래프 생성
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 리프 노드의 깊이의 합을 저장할 변수
answer = 0
# 방문한 노드는 더이상 방문할 필요가 없다. 아직 아무 노드도 방문하지 않았으므로 전부 False.
visited = [False] * (N + 1)

# 현재 노드와 현재 노드의 깊이.


def DFS(node, depth):
    # 함수가 끝난 후에도 answer의 값을 유지하기 위해 global로 설정
    global answer
    # 방문한 노드는 True로 변경
    visited[node] = True
    # 해당 노드가 리프 노드인지 확인할 플래그. 밑에서 리프노드가 아니라면 False로 바꿔줄 것이다.
    is_Leaf = True

    # 해당 노드의 자식 노드들을 확인하면서
    for child in graph[node]:
        # 자식 노드에 아직 방문하지 않았다면
        if not visited[child]:
            # DFS 실행. 자식 노드이므로 깊이가 1 증가한다.
            DFS(child, depth+1)
            # 자식 노드가 있다는 것은 리프 노드가 아니라는 뜻이다.
            is_Leaf = False

    # 해당 노드가 리프 노드라면
    if is_Leaf:
        # 해당 노드까지의 깊이를 answer에 저장
        answer += depth


# DFS를 실행한다. 1번 노드를 루트로 삼고 루트의 깊이는 0이다.
DFS(1, 0)

# 이번 문제에서 가장 기저가 되는 풀이법은 각 리프 노드까지의 깊이의 합이 홀수여야 한다는 것이다.
# 따라서 answer을 2로 나누었을 때 나누어 떨어지지 않으면 Yes를, 나누어 떨어지면 No를 출력한다.
print("Yes" if answer % 2 == 1 else "No")


''' 주석 없는 코드
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [False] * (N + 1)

def DFS(node, depth):
    global answer
    visited[node] = True
    is_Leaf = True

    for child in graph[node]:
        if not visited[child]:
            DFS(child, depth+1)
            is_Leaf = False

    if is_Leaf:
        answer += depth

DFS(1, 0)

print("Yes" if answer % 2 == 1 else "No")
'''
