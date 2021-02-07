"""
LeetCode 819. Most Common Word
url: https://leetcode.com/problems/most-common-word/
writer: Harim Kang
Language: Python3
Date: 2021.02.04
Status: Success, Runtime: 36 ms, Memory Usage: 14 MB
"""


def solution(triangle):
    dp = [[0 for _ in triangle[i]] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[-1])


if __name__ == "__main__":
    inputs = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]]
    expected = [30]
    resp = []
    for tri in inputs:
        resp.append(solution(tri))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
