"""
Baekjoon 14888. 연산자 끼워넣기
url: https://www.acmicpc.net/problem/14888
writer: Harim Kang
Language: Python3
Date: 2021.02.21
Status: Success, Runtime: 640 ms, Memory Usage: 34252 KB
"""

# input을 받는 코드 : N, M, V
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


def dfs(cnt, result, p, m, mul, div, min_val, max_val):
    if cnt == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return min_val, max_val
    if p:
        dfs(cnt + 1, result + nums[cnt], p - 1, m, mul, div, min_val, max_val)
    if m:
        dfs(cnt + 1, result - nums[cnt], p, m - 1, mul, div, min_val, max_val)
    if mul:
        dfs(cnt + 1, result * nums[cnt], p, m, mul - 1, div, min_val, max_val)
    if div:
        dfs(
            cnt + 1,
            -(-result // nums[cnt]) if result < 0 else result // nums[cnt],
            p,
            m,
            mul,
            div - 1,
            min_val,
            max_val,
        )


max_v = -(10 ** 8) - 1
min_v = 10 ** 8 + 1
min_v, max_v = dfs(1, nums[0], add, sub, mul, div, min_v, max_v)

print(max_v)
print(min_v)
