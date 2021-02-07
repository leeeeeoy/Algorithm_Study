"""
LeetCode 819. Most Common Word
url: https://leetcode.com/problems/most-common-word/
writer: Harim Kang
Language: Python3
Date: 2021.02.04
Status: Success, Runtime: 36 ms, Memory Usage: 14 MB
"""
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        word = [
            w
            for w in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if w not in banned
        ]
        count = collections.Counter(word)
        answer = count.most_common(1)[0][0]

        return answer


if __name__ == "__main__":
    inputs = [["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]]]
    expected = ["ball"]
    resp = []
    sol = Solution()
    for p, b in inputs:
        resp.append(sol.mostCommonWord(p, b))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
