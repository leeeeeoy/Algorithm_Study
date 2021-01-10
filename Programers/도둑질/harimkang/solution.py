"""
Programmers 42897. thievery
url: https://programmers.co.kr/learn/courses/30/lessons/42897
writer: Harim Kang
Language: Python3
Date: 2021.01.08
Status: Success
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
"""


def solution(money):

    answer = []

    # 첫번째 집에 방문하는 경우
    dp = [0 for _ in money]
    dp[0] = dp[1] = money[0]
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    # 첫번째를 안가고 두번째를 방문하는 경우
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    # 첫번째 두번째 모두 안가는 경우
    dp[0] = dp[1] = 0
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer.append(max(dp))

    return max(answer)


if __name__ == "__main__":
    test_cases = [[1, 2, 3, 1], [10, 2, 2, 100, 2]]
    expected = [4, 110]
    for i in range(len(test_cases)):
        _m = test_cases[i]
        expect = expected[i]
        ans = solution(_m)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
