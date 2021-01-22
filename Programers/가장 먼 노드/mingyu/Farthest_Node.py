"""
Programmers. 가장 먼 노드
url: https://programmers.co.kr/learn/courses/30/lessons/49189
writer: Mingyu
Language: Python3
Date: 2021.01.21
Status: , Runtime:  ms, Memory Usage:  KB
"""

# BFS를 효율적으로 사용하기 위해 deque 사용
from collections import deque

def solution(n, edge):
    # graph를 딕셔너리로 선언
    graph = dict()

    # 양방향 그래프이므로 양 노드를 서로 연결해준다.
    # setdefault는 키 값과 값 하나를 인자로 받는 dict의 메소드이다. 해당 키 값이 없다면 키와 값을 넣고, 키가 있다면 값을 업데이트한다.
    for x, y in edge:
        # 키는 x, 값은 빈 리스트를 설정하여 값에 y들이 들어올 수 있도록 한다. 반대의 경우도 동일.
        graph.setdefault(x, []).append(y)
        graph.setdefault(y, []).append(x)

    # 시작 노드는 1번이고, 1번 노드에서 1번 노드까지의 거리는 0이다. [노드 번호, 현재 노드까지의 거리]
    queue = deque([[1, 0]])
    # [-1]로 설정하는 이유는 해당 노드에 대한 방문 여부를 체크하기 위함이다.
    # 길이를 n이 아니라 n+1으로 설정하는 이유는 노드 번호가 1부터 시작하기 때문.
    check = [-1] * (n + 1)

    # queue가 빌 때까지
    while queue:
        # 노드 번호, 현재 노드까지의 거리. 일반적인 list.pop(0)은 효율성이 O(N)이라 효율적이지 않다. deque의 popleft는 O(1).
        index, depth = queue.popleft()

        # 시작 노드부터 방문한 노드까지의 깊이(거리)를 저장
        check[index] = depth

        for i in graph[index]:
            # 방문하지 않은 노드라면
            if check[i] == -1:
                # 방문했다는 표시를 함과 동시에 현재까지의 거리를 넣어주어야 하기 때문에 0으로 만든 후
                check[i] = 0
                # queue에 해당 노드 인덱스와 시작 노드부터 1칸 멀어졌다는 깊이를 넣어준다.
                queue.append([i, depth + 1])

        # 깊이 증가
        depth += 1

    # check 배열에서 가장 높은 숫자, 즉 가장 먼 거리에 있는 노드들의 수가 여러개라면 그만큼을 count하여 반환
    return check.count(max(check))


''' 주석 없는 코드
from collections import deque

def solution(n, edge):
    graph = dict()

    for x, y in edge:
        graph.setdefault(x, []).append(y)
        graph.setdefault(y, []).append(x)

    queue = deque([[1, 0]])
    check = [-1] * (n + 1)

    while queue:
        index, depth = queue.popleft()
        check[index] = depth
        for i in graph[index]:
            if check[i] == -1:
                check[i] = 0
                queue.append([i, depth + 1])
        depth += 1

    return check.count(max(check))
'''