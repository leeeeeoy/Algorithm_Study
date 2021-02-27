"""
LeetCode 761. Special Binary String
url: https://leetcode.com/problems/special-binary-string/
writer: Harim Kang
Language: Python3
Date: 2021.02.09
Status: Success, Runtime: 28 ms, Memory Usage: 14.6 MB
"""


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        result = []
        i, balance = 0, 0
        for j in range(len(S)):
            if S[j] == "1":
                # 1인 경우 balance += 1
                balance += 1
            else:
                # 0인 경우 balace -= 1
                balance -= 1

            if balance == 0:
                # 0과 1의 갯수가 맞는 경우
                print(f"i = {i}, j = {j}")
                print(S[i + 1 : j])
                subString = self.makeLargestSpecial(S[i + 1 : j])
                result.append(f"1{subString}0")
                i = j + 1
                print(i)
            print(result)

        result.sort()
        return "".join(result[::-1])


if __name__ == "__main__":
    inputs = ["11011000"]
    expected = ["11100100"]
    resp = []
    sol = Solution()
    for input in inputs:
        resp.append(sol.makeLargestSpecial(input))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)