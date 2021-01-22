"""
Baekjoon 2306. 유전자
url: https://www.acmicpc.net/problem/2306
writer: Harim Kang
Language: Python3
Date: 2021.01.09
Status: Success, Runtime: 488 ms, Memory Usage: 125404 KB
"""

dna = input()
dp = [[0 for _ in dna] for _ in dna]

for i in range(1, len(dna)):
    for s in range(len(dna) - i):

        # i는 확인하려는 문자의 수
        # s는 현재 문자의 시작 위치, e는 문자의 끝
        e = s + i
        if (dna[s] == "a" and dna[e] == "t") or (dna[s] == "g" and dna[e] == "c"):
            # 현재 확인 문자의 양끝이 a,t 이거나 g,c인 경우
            # 글자가 하나씩 줄었을때보다 2 증가
            dp[s][e] = dp[s + 1][e - 1] + 2

        for j in range(s, e):
            # j는 현재 확인 문자의 중간 부분을 도는 인덱스
            # 한바퀴 돌면서 가장 큰 걸 지정해준다.
            dp[s][e] = max(dp[s][e], dp[s][j] + dp[j + 1][e])

print(dp[0][len(dna) - 1])