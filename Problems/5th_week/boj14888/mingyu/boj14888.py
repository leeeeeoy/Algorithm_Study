"""
BaekJoon 14888. 연산자 끼워넣기
url: https://www.acmicpc.net/problem/14888
writer: Mingyu
Language: Python3
Date: 2021.02.09
Status: , Runtime:  ms, Memory Usage:  KB
"""

import sys

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최대, 최소 값을 저장할 변수. 비교 시 프로그램에 영향을 끼치지 않도록 maxv에는 가장 작은 값을, minv에는 가장 큰 값을 부여
maxv = -sys.maxsize - 1
minv = sys.maxsize

# 백트래킹
# calc(현재 인덱스, 다음 인덱스에 해당하는 숫자, 덧셈, 뺄셈, 곱셈, 나눗셈 연산)


def calc(index, num, add, sub, mul, div):
    # 함수 바깥에서 불러온 후 함수 종료 후에도 계속 쓰는 변수이기 때문에 global로 설정
    global N, maxv, minv

    # index는 아래 재귀함수를 돌면서 N까지 증가하게 된다.
    # index가 N이 되었다는 것은 numbers를 다 탐색한 이후라는 뜻이다.(N = len(numbers))
    if index == N:
        # 끝까지 탐색이 완료되었다면 이전 재귀를 돌면서 저장했던 maxv, minv와 비교하여 각자 크고 작은 값을 업데이트한다.
        maxv = max(num, maxv)
        minv = min(num, minv)
        return

    # 각 사칙연산을 수행, 인덱스를 증가 후 현재 숫자와 다음 숫자를 각 사칙연산에 맞게 수행
    # 수행한 사칙연산의 개수를 하나씩 제거한다.
    else:
        if add:
            calc(index + 1, num + numbers[index], add - 1, sub, mul, div)

        if sub:
            calc(index + 1, num - numbers[index], add, sub - 1, mul, div)

        if mul:
            calc(index + 1, num * numbers[index], add, sub, mul - 1, div)

        if div:
            calc(index + 1, int(num / numbers[index]), add, sub, mul, div - 1)


calc(1, numbers[0], add, sub, mul, div)

print(maxv, minv)


''' 주석 없는 코드

import sys

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxv = -sys.maxsize - 1
minv = sys.maxsize

def calc(index, num, add, sub, mul, div):
    global N, maxv, minv

    if index == N:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return

    else:
        if add:
            calc(index + 1, num + numbers[index], add - 1, sub, mul, div)

        if sub:
            calc(index + 1, num - numbers[index], add, sub - 1, mul, div)

        if mul:
            calc(index + 1, num * numbers[index], add, sub, mul - 1, div)

        if div:
            calc(index + 1, int(num / numbers[index]), add, sub, mul, div - 1)


calc(1, numbers[0], add, sub, mul, div)

print(maxv, minv)
'''
