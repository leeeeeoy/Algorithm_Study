"""
Programmers 1845. 폰켓몬
url: https://programmers.co.kr/learn/courses/30/lessons/1845
writer: Harim Kang
Language: Python3
Date: 2021.02.27
Status: Success, Runtime: 640 ms, Memory Usage: 34252 KB
"""


def solution(nums):
    if len(list(set(nums))) < len(nums) // 2:
        return len(list(set(nums)))
    return len(nums) // 2


if __name__ == "__main__":
    inputs = [[3, 1, 2, 3], [3, 3, 3, 2, 2, 4], [3, 3, 3, 2, 2, 2]]
    expected = [2, 3, 2]
    resp = []
    for input in inputs:
        resp.append(solution(input))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)