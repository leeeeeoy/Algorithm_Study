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
def calc(index, num, add, sub, mul, div):
    global N, maxv, minv

    if index == N:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return

    else:
        if add:
            print("add", end=" ")
            calc(index + 1,num + numbers[index], add - 1, sub, mul, div)
            
        if sub:
            print("sub", end=" ")
            calc(index + 1, num - numbers[index], add, sub - 1, mul, div)
            
        if mul:
            print("mul", end=" ")
            calc(index + 1, num * numbers[index], add, sub, mul - 1, div)
            
        if div:
            print("div", end=" ")
            calc(index + 1, int(num / numbers[index]), add, sub, mul, div - 1)
        
        print()
            


calc(1, numbers[0], add, sub, mul, div)

print(maxv, minv)
