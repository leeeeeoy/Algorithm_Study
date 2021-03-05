"""
Programmers. 자물쇠와 열쇠
url: https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
writer: Mingyu
Language: Python3
Date: 2021.03.03
Status: , Runtime:  ms, Memory Usage:  KB
"""

# 2차원 배열을 90도 회전하는 함수


def rotate(arr):
    length = len(arr)
    # ret 배열을 0으로 해당 2차원 배열의 크기에 맞게 초기화한 후
    ret = [[0] * length for _ in range(length)]

    # 90도 회전한 값을 ret에 넣는다.
    for row in range(length):
        for col in range(length):
            ret[col][length - 1 - row] = arr[row][col]

    return ret


# key가 lock에 들어맞는지 확인하는 함수
# check(key의 x좌표, key의 y좌표, key, lock, 확장된 사이즈, 자물쇠의 시작점, 자물쇠의 끝점)
def check(keyX, keyY, key, lock, expendSize, lock_start, lock_end):
    # 확장사이즈에 맞추어 확장된 리스트를 0으로 초기화하여 만듬
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # 확장된 배열의 전체 부분을 key로 완전탐색할 것이다.
    for i in range(len(key)):
        for j in range(len(key)):
            # 인자로 받아온 key의 x, y좌표를 기준으로 key를 넣는다
            expendList[keyX + i][keyY + j] += key[i][j]

    #  자물쇠가 열리는지 확인하는 부분
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            # key가 expendList에 이미 들어와있는 상태에서, lock을 expendList에 넣어본다
            expendList[i][j] += lock[i - lock_start][j - lock_start]
            # 만일 0이 나온다면 key가 lock에 들어맞지 않았다는 뜻이므로 False를 return
            if expendList[i][j] == 0:
                return False

    # for문을 통과했다면 열쇠가 들어맞았다는 뜻이므로 True를 return
    return True


def solution(key, lock):
    # 자물쇠의 시작점. lock 주변을 key 배열로 확장하기 때문에 key의 마지막이 lock의 첫번째가 된다.
    lock_start = len(key) - 1
    # 자물쇠의 끝점. 시작점에서 lock의 길이만큼 추가
    lock_end = lock_start + len(lock)
    # 확장 사이즈. key가 lock을 한 칸 겹치는 모양으로 주변을 둘러싸기 때문에 lock의 길이에 (len(key)-1 )*2를 더해준다. 좌우를 포함하기 때문에 *2이다.
    expendSize = len(lock) + lock_start * 2

    # 열쇠를 0, 90, 180, 270도로 4번 돌려보면서
    for _ in range(4):
        # 자물쇠를 확인했을 때
        for i in range(lock_end):
            for j in range(lock_end):
                # key가 자물쇠에 들어맞는다면 True를 return
                if check(i, j, key, lock, expendSize, lock_start, lock_end):
                    return True

        # 아직 들어맞지 않았다면 key를 돌려본다
        key = rotate(key)

    # for문을 통과했다면 들어맞는 부분이 없다는 뜻이다. 그러므로 False를 return
    return False


''' 주석 없는 코드

def rotate(arr):
    length = len(arr)
    ret = [[0] * length for _ in range(length)]

    for row in range(length):
        for col in range(length):
            ret[col][length - 1 - row] = arr[row][col]

    return ret


def check(keyX, keyY, key, lock, expendSize, lock_start, lock_end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    for i in range(len(key)):
        for j in range(len(key)):
            expendList[keyX + i][keyY + j] += key[i][j]

    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            expendList[i][j] += lock[i - lock_start][j - lock_start]
            if expendList[i][j] != 1:
                return False

    return True


def solution(key, lock):
    lock_start = len(key) - 1
    lock_end = lock_start + len(lock)
    expendSize = len(lock) + lock_start * 2

    for _ in range(4):
        for i in range(lock_end):
            for j in range(lock_end):
                if check(i, j, key, lock, expendSize, lock_start, lock_end):
                    return True

        key = rotate(key)

    return False
'''
