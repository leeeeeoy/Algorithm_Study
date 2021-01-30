"""
LeetCode 997. Find the Town Judge
url: https://leetcode.com/problems/find-the-town-judge/
writer: Harim Kang
Language: Python3
Date: 2021.01.29
Status: Success, Runtime: 724 ms, Memory Usage: 19.1 MB
"""


class Solution:
    def findJudge(self, N, trust) -> int:
        people = [1 for _ in range(N)]
        candi = [0 for _ in range(N)]

        for a, b in trust:
            people[a - 1] = 0
            candi[b - 1] += 1

        if 1 in people and candi[people.index(1)] == N - 1:
            return people.index(1) + 1
        else:
            return -1


if __name__ == "__main__":
    inputs = [
        [2, [[1, 2]]],
        [3, [[1, 3], [2, 3]]],
        [3, [[1, 3], [2, 3], [3, 1]]],
        [3, [[1, 2], [2, 3]]],
        [4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]],
    ]
    expected = [2, 3, -1, -1, 3]
    resp = []
    sol = Solution()
    for N, trust in inputs:
        ans = sol.findJudge(N, trust)
        resp.append(ans)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
