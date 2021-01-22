"""
LeetCode. 마을 판사를 찾아라
url: https://leetcode.com/problems/find-the-town-judge/
writer: Mingyu
Language: Python3
Date: 2021.01.20
Status: , Runtime:  ms, Memory Usage:  KB
"""

""" 문제
* 이 마을에는 1부터 N까지의 사람이 살고 있다.

* 1. 마을 판사는 아무도 믿지 않는다.
* 2. 마을 판사를 제외한 모든 사람들은 마을 판사를 믿는다
* 3. 1, 2번 조건을 만족하는 사람은 단 한명 뿐이다.

* trust[i] = [a, b]는 a가 b를 신뢰한다는 뜻이다.
* 마을 판사가 존재하며 신원 확인이 되는 경우 마을 판사를 반환하고, 그렇지 않으면 -1을 반환하라
"""

def findJudge(N, trust):
    # 사람의 수가 두 명 이상인데 서로를 신뢰하지 않는다면 조건 2를 만족하지 않는다.
    if N > 1 and not trust:
        return -1

    # 재귀를 사용한 DFS 알고리즘. 해당 알고리즘에 대한 자세한 설명은 "Baekjoon\boj11724\mingyu\boj11724.py"를 참조
    def DFS(node):
        visited[node] = True
        for i in town[node]:
            if not visited[node]:
                DFS(i)

    # 방문이 확인된 노드 배열
    visited = [False] * (N + 1)

    # 각 마을 사람들이 신뢰하고 있는 사람들의 배열 
    town = [[] for _ in range(N + 1)]

    # trust[i] = [a, b]는 a가 b를 신뢰한다는 뜻이다. 이를 단방향 그래프 형태로 구현
    for a, b in trust:
        town[a].append(b)

    # 각 마을 사람들이 누구를 신뢰하고 있는지에 대한 그래프를 DFS를 통해 정립
    for i in range(1, N + 1):
        if not visited[i]:
            DFS(i)

    # 아직 아무도 신뢰관계가 확인되지 않은 상태이므로 -1을 초기값으로 둔다.
    answer = -1

    # 각 사람들이 누구를 믿고 있는지 확인하기 위한 배열
    check = []

    # 마을 사람들이 누구를 믿고 있는지 확인한다.
    for i in range(1, N + 1):
        # 아무도 믿지 않는 사람이 있다면 조건 1에 따라 해당 사람이 마을 판사로 추정된다. answer에 해당 사람(i)를 집어넣자.
        if not town[i]:
            answer = i

        # i번째 사람이 누군가를 믿고 있다면 i가 믿고 있는 사람들의 목록을 check에 넣어둔다.
        else:           
            check.append(town[i])

    # 조건 2의 모든 사람들은 마을 판사를 믿는다는 명제를 확인하는 부분이다.
    # answer은 현재 마을 판사로 추정되는 사람이다.
    for i in check:
        # 모두가 마을 판사를 믿고 있어야 하는데, 누군가 answer를 믿고 있지 않다면 answer는 마을 판사가 아니다. 즉 마을 판사가 존재하지 않으므로 -1을 return
        if answer not in i:
            return -1

    # 위의 조건 2 구문을 통과했으면 마을 판사가 맞다.
    return answer


''' 주석 없는 코드
def findJudge(N, trust):

    if N > 1 and not trust:
        return -1

    def DFS(node):
        visited[node] = True
        for i in town[node]:
            if not visited[node]:
                DFS(i)

    visited = [False] * (N + 1)
    town = [[] for _ in range(N + 1)]

    for a, b in trust:
        town[a].append(b)

    for i in range(1, N + 1):
        if not visited[i]:
            DFS(i)

    answer = -1
    check = []
    for i in range(1, N + 1):
        if not town[i]:
            answer = i
        else:           
            check.append(town[i])

    for i in check:
        if answer not in i:
            return -1

    return answer
'''