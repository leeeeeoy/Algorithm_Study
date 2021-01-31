"""
Baekjoon 14425. 문자열 집합
url: https://www.acmicpc.net/problem/14425
writer: Mingyu
Language: Python3
Date: 2021.01.26
Status: , Runtime:  ms, Memory Usage:  KB
"""

import sys


N, M = map(int, sys.stdin.readline().split())

# 검사의 기준이 되는 문자열
standard = [sys.stdin.readline().strip() for _ in range(N)]

# 검사받아야 할 문자열
check = [sys.stdin.readline().strip() for _ in range(M)]

# 검사 기준에 부합하는(포함되는) 문자열의 개수를 담을 변수
cnt = 0

# 검사받아야 할 문자열을 하나씩 돌면서
for i in check:
    # 해당 문자열이 검사 기준에 부합한다면
    if i in standard:
        # 개수 추가
        cnt += 1
        # 찾았으니 뒤에는 더 볼 필요 없이 다음 문자열로 간다.
        continue

print(cnt)


''' 주석 없는 코드
import sys

N, M = map(int, sys.stdin.readline().split())

standard = [sys.stdin.readline().strip() for _ in range(N)]
check = [sys.stdin.readline().strip() for _ in range(M)]

cnt = 0

for i in check:
    if i in standard:
        cnt += 1
        continue
    
print(cnt)
'''
