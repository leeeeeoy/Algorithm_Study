"""
programmers 12905. 가장 큰 정사각형 찾기
url: https://programmers.co.kr/learn/courses/30/lessons/12905
writer: Harim Kang
Language: Python3
Date: 2021.02.09
Status: Success, Runtime: 28 ms, Memory Usage: 14.6 MB
"""


def solution(board):
    # Write your code here
    answer = 0
    # check all zeros
    for i in range(len(board)):
        if board[i][0] == 1:
            answer = 1
            continue
    for j in range(len(board[0])):
        if board[0][j] == 1:
            answer = 1
            continue

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = (
                    min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                )
            if board[i][j] ** 2 > answer:
                answer = board[i][j] ** 2
    return answer


if __name__ == "__main__":
    inputs = [
        [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]],
        [[0, 0, 1, 1], [1, 1, 1, 1]],
    ]
    expected = [9, 4]
    resp = []
    for input in inputs:
        resp.append(solution(input))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)