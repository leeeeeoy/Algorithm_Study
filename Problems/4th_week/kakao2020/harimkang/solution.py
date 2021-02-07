"""
kakao2020. 문자열 압축
url: https://programmers.co.kr/learn/courses/30/lessons/60057
writer: Harim Kang
Language: Python3
Date: 2021.02.06
Status: Success
"""


def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        candiStr = ""
        num = 1
        temp = s[:size]
        i = size
        while i < len(s):
            if s[i : i + size] == temp:
                num += 1
            else:
                if num == 1:
                    candiStr += temp
                else:
                    candiStr += str(num) + temp
                temp = s[i : i + size]
                num = 1
            i += size
        if num == 1:
            candiStr += temp
        else:
            candiStr += str(num) + temp

        if answer > len(candiStr):
            answer = len(candiStr)

    return answer


if __name__ == "__main__":
    inputs = [
        "aabbaccc",
        "ababcdcdababcdcd",
        "abcabcdede",
        "abcabcabcabcdededededede",
        "xababcdcdababcdcd",
    ]
    expected = [7, 9, 8, 14, 17]
    resp = []
    for _s in inputs:
        resp.append(solution(_s))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
