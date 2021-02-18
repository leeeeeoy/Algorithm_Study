"""
Programmers. 크레인 인형뽑기 게임
url: https://programmers.co.kr/learn/courses/30/lessons/64061
writer: Mingyu
Language: Python3
Date: 2021.02.10
Status: , Runtime:  ms, Memory Usage:  KB
"""

from collections import deque


def solution(board, moves):
    # 사라진 인형의 개수
    answer = 0

    # moves는 열(col)의 인덱스와 같은데, 인덱스는 0부터 시작하고 moves는 1부터 시작하므로 모두 1을 빼서 인덱스 번호와 맞춰준다.
    # popleft를 사용하기 위해 deque으로 설정. pop(0)은 시간 복잡도가 O(n)이지만 popleft()는 시간 복잡도가 O(1)이다.
    moves = deque([i - 1 for i in moves])

    # 뽑은 인형들을 넣을 스택
    basket = []

    # 움직임이 끝날 때까지
    while moves:
        # moves의 첫 번째 원소를 가져온다.
        crain = moves.popleft()

        # 인형을 잡고 있는지에 대한 플래그
        getFlag = False

        # 보드를 돌면서
        for row in range(len(board)):
            for col in range(len(board[row])):

                # col == crain : 크레인이 뽑을 열과 현재 열이 일치하고
                # board[row][col] : 해당 칸에 인형(값)이 존재하면서
                # not getFlag : 아직 인형을 잡지 않았을 경우
                if col == crain and board[row][col] and not getFlag:

                    # 바구니에 해당 인형을 넣고
                    basket.append(board[row][col])
                    # 해당 칸은 비어있음으로 바꿈
                    board[row][col] = 0
                    # 인형을 집었으니 flag를 변경
                    getFlag = True

                    # 바구니에 인형이 2개 이상 있을 경우
                    if len(basket) >= 2:

                        # 방금 뽑은 인형과 마지막에 뽑았던 인형이 같다면
                        if basket[-2] == basket[-1]:

                            # 두 인형을 제거하고 사라진 인형 수 2 만큼 answer을 증가
                            basket.pop()
                            basket.pop()
                            answer += 2

    return answer


''' 주석 없는 코드

from collections import deque


def solution(board, moves):
    answer = 0
    moves = deque([i - 1 for i in moves])
    basket = []

    while moves:
        crain = moves.popleft()
        getFlag = False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if col == crain and board[row][col] and not getFlag:
                    basket.append(board[row][col])
                    board[row][col] = 0
                    getFlag = True

                    if len(basket) >= 2:
                        if basket[-2] == basket[-1]:
                            basket.pop()
                            basket.pop()
                            answer += 2

    return answer
'''
