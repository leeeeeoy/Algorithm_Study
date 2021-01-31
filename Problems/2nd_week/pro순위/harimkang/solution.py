"""
Programmers 49191. 순위
url: https://programmers.co.kr/learn/courses/30/lessons/49191
writer: Harim Kang
Language: Python3
Date: 2021.01.29
Status: Success
정확성: 100.0
합계: 100.0 / 100.0
"""
import collections


def solution(n, results):
    answer = 0

    # 얘네는 이긴다 :  winner
    winner = collections.defaultdict(list)
    # 얘네는 못이긴다 : losser
    losser = collections.defaultdict(list)

    for win, loss in results:
        if loss not in winner[win]:
            winner[win].append(loss)
        if win not in losser[loss]:
            losser[loss].append(win)

    for i in range(n):
        for w in winner[i + 1]:
            losser[w].extend(losser[i + 1])
        for l in losser[i + 1]:
            winner[l].extend(winner[i + 1])

    for i in range(n):
        if len(set(winner[i + 1])) + len(set(losser[i + 1])) == n - 1:
            answer += 1

    return answer


if __name__ == "__main__":
    inputs = [
        [5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]],
    ]
    expected = [2]
    resp = []
    for n, result in inputs:
        ans = solution(n, result)
        resp.append(ans)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)