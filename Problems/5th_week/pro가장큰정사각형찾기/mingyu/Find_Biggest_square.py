"""
Programmers. 가장 큰 정사각형 찾기
url: https://programmers.co.kr/learn/courses/30/lessons/12905
writer: Mingyu
Language: Python3
Date: 2021.02.15
Status: , Runtime:  ms, Memory Usage:  KB
"""
# 배열의 전체 원소를 한 리스트로 합치기 위해 사용한 모듈
from itertools import chain

def solution(board):
    # 2*2 크기의 정사각형의 우측 하단을 기준으로 검사할 것이다. 그렇기 때문에 (0, 0)번째 인덱스는 버리므로 행과 열 둘 다 1부터 시작한다.
    for row in range(1, len(board)):
        for col in range(1, len(board[row])):
            # 해당 인덱스에 들어있는 수가 1 이상이라면
            if board[row][col] >= 1:
                # 우측 하단을 기준으로 삼았으니 좌측, 상단, 좌상단의 인덱스에 들어있는 값을 확인한다. 
                # 이 중 가장 작은 값에 +1을 하여 해당 인덱스에서의 숫자를 업데이트
                # 가장 작은 수를 기준으로 하여 +1을 하게 되면 검사하는 수에 0이 있더라도 원래 현 인덱스에 들어있던 값인 1로 업데이트 된다
                # 현 인덱스가 1이고 다른 모든 인덱스가 n이상이면 n+1의 수를 현 인덱스에 업데이트한다.
                # 이 때 n+1은 해당 인덱스를 기준으로 한 정사각형의 너비이자 높이가 된다.
                board[row][col] = min(board[row-1][col], board[row][col-1], board[row-1][col-1]) + 1

    # 인덱스의 값을 추가하면서 board에 저장하였으니, 이 board를 전체 검사하기 위해 chain.from_iterable을 사용하여 한 리스트로 묶은 후
    # 가장 큰 값을 뽑아 제곱을 해준다. 정사각형(너비=높이)의 크기를 구하는 문제이기 때문에 이를 구하기 위해선 너비 * 높이가 되어야 하기 때문.
    return max(chain.from_iterable(board)) ** 2



''' 주석 없는 코드

from itertools import chain

def solution(board):
    for row in range(1, len(board)):
        for col in range(1, len(board[row])):
            if board[row][col] >= 1:
                board[row][col] = min(board[row-1][col], board[row][col-1], board[row-1][col-1]) + 1

    return max(chain.from_iterable(board)) ** 2
'''