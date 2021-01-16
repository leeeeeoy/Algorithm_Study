"""
Baekjoon 1695. 팰린드롬 만들기
url: https://www.acmicpc.net/problem/1695
writer: Harim Kang
Language: Python3
Date: 2021.01.08
Status: , Runtime:  ms, Memory Usage:  KB
"""

# input을 받는 코드 : N
N = int(input())
num_list = list(map(int, input().split()))
# N = 5
# num_list = [1, 2, 3, 4, 2]

# i, j자리의 숫자를 비교해서 같으면 한칸씩 줄이고, 다르면 1개를 추가해야한다는 의미로, +1 해주고 한쪽만 줄이는 방식
dp = [[None for _ in range(N)] for _ in range(N)]


def palindrome(i, j):
    if dp[i][j] is not None:
        return dp[i][j]
    if i >= j:
        dp[i][j] = 0
        return 0
    else:
        if num_list[i] == num_list[j]:
            dp[i][j] = palindrome(i + 1, j - 1)
        else:
            dp[i][j] = min(palindrome(i + 1, j), palindrome(i, j - 1)) + 1

        return dp[i][j]


if num_list == num_list[::-1]:
    print(0)
else:
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            palindrome(i, j)

    print(dp[0][N - 1])
