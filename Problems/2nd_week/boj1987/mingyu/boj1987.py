"""
Baekjoon 1987. 알파벳
url: https://www.acmicpc.net/problem/1987
writer: Mingyu
Language: Python3
Date: 2021.01.19
Status: , Runtime:  ms, Memory Usage:  KB
"""


import sys

# 좌 우 상 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    # 말이 지나는 칸은 좌측 상단의 칸, 즉 첫번째 알파벳도 포함한다고 한다. 때문에 시작값은 첫번째 알파벳의 길이인 1로 설정한다.
    answer = 1
    # 너비우선탐색을 위한 큐 생성
    # 같은 알파벳이 여러개 들어올 필요는 없다. 그러니 set으로 설정
    # 시작값은 좌측 상단이라고 했으니 초기값을 튜플 형태의 (0, 0, board[0][0])으로 설정
    queue = set([(0, 0, board[0][0])])

    # 큐가 빌 때까지
    while queue:
        # queue에서 x, y좌표와 해당 위치에 있는 알파벳을 가져온다.
        x, y, ans = queue.pop()

        # 상하좌우로 움직이면서
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 움직였을 때 해당 위치로 이동할 수 있다면(index를 벗어나지 않는다면), 해당 칸에 있는 알파벳이 중복되는지 확인한다.
            if((0 <= nx < row) and (0 <= ny < col)) and (board[nx][ny] not in ans):
                # 조건을 통과했다면 queue에 이동한 위치를 추가하고, 문자열 ans에 알파벳을 하나 더해준다.
                queue.add((nx, ny, ans + board[nx][ny]))
                # 지금까지 지나온 거리(answer)와 현재 노드로 온 거리(len(ans)+1)중 더 멀리 온 것을 선택
                # 위의 ans + board[nx][ny]는 queue에 삽입하는 과정에서 일어난 것이다. ans의 메모리 자체는 변경되지 않은 것.
                # 때문에 ans에 board[nx][ny]를 추가한 길이인 len(ans) + 1을 비교 대상으로 넣는 것이다.
                answer = max(answer, len(ans) + 1)

    return answer


# 행렬과 보드를 입력받는다
row, col = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(row)]

# BFS는 answer를 리턴하기 때문에 이대로 출력하면 된다.
print(BFS(0, 0))



''' 주석 없는 코드
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    answer = 1
    queue = set([(0, 0, board[0][0])])

    while queue:
        x, y, ans = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if((0 <= nx < row) and (0 <= ny < col)) and (board[nx][ny] not in ans):
                queue.add((nx, ny, ans + board[nx][ny]))
                answer = max(answer, len(ans) + 1)

    return answer

row, col = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(row)]

print(BFS(0, 0))
'''