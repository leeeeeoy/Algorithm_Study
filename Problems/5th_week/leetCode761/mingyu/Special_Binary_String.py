"""
LeetCode 761. 특수 이진 문자열
url: https://leetcode.com/problems/special-binary-string/
writer: Mingyu
Language: Python3
Date: 2021.02.18
Status: , Runtime:  ms, Memory Usage:  KB
"""

# 이해하지 못함.
def makeLargestSpecial(S):
    count = i = 0
    res = []
    for j, v in enumerate(S):
        count = count + 1 if v=='1' else count - 1
        if count == 0:
            # 이 부분을 이해하지 못했습니다
            res.append('1' + makeLargestSpecial(S[i + 1:j]) + '0')
            i = j + 1
    return ''.join(sorted(res)[::-1])

print(makeLargestSpecial("11011000"))