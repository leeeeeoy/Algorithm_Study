"""
LeetCode 5. 가장 긴 팰린드롬 문자열
url: https://leetcode.com/problems/longest-palindromic-substring/
writer: Mingyu
Language: Python3
Date: 2021.03.04
Status: , Runtime:  ms, Memory Usage:  KB
"""

s = "aaaaa"


def longestPalindrome(s):
    if len(s) <= 1:
        return s

    # substring의 시작 index와 길이. 처음엔 0으로 초기화
    sub_idx, sub_len = 0, 0

    # s를 순회하면서
    for j in range(len(s)):
        # j - sub_len을 하면 substring의 시작점인 sub_idx가 나오고, 여기서부터 문자 하나를 더해(j + 1) 문자열을 역전시킨 것([::-1])과 동일하다면
        # 해당 j - sun_len을 sub_indx로 설정하고, 문자를 하나 더한 것이 팰린드롬을 이루므로 sub_len+1을 해준다.
        if s[j - sub_len: j + 1] == s[j - sub_len: j + 1][::-1]:
            sub_idx, sub_len = j-sub_len, sub_len+1

        # sub_len이 j보다 크지 않은 시점에서 substring의 좌우를 늘린 상태로 역전된 문자열과 비교했을 때 동일하다면
        elif j - sub_len > 0 and s[j - sub_len-1: j + 1] == s[j-sub_len - 1: j + 1][::-1]:
            # sub_idx를 업데이트하고 길이는 좌우를 늘렸으므로 2를 더한다
            sub_idx, sub_len = j-sub_len - 1, sub_len + 2

    # substring의 시작점(sub_idx)부터 sub_len만큼 가져오면 팰린드롬인 substring이 나온다.
    return s[sub_idx: sub_idx+sub_len]


print(longestPalindrome(s))


''' 주석 없는 코드

def longestPalindrome(s):
    if len(s) <= 1:
        return s

    sub_idx, sub_len = 0, 0

    for j in range(len(s)):
        if s[j - sub_len: j + 1] == s[j - sub_len: j + 1][::-1]:
            sub_idx, sub_len = j-sub_len, sub_len+1

        elif j - sub_len > 0 and s[j - sub_len-1: j + 1] == s[j-sub_len - 1: j + 1][::-1]:
            sub_idx, sub_len = j-sub_len - 1, sub_len + 2

    return s[sub_idx: sub_idx+sub_len]
'''
