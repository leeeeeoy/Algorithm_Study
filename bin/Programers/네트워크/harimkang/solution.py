"""
Programmers 43162. Network
url: https://programmers.co.kr/learn/courses/30/lessons/43162
writer: Harim Kang
Language: Python3
Date: 2021.01.08
Status: Success
정확성: 100.0
합계: 100.0 / 100.0
"""


def solution(n, computers):

    # dfs방식으로, 노드를 하나씩 방문하면서 방문 여부를 체크하는 함수
    def dfs(s):
        # s는 시작 노드를 의미한다. 스택을 사용하여 구현
        stack = [s]

        while stack:
            # stack이 빌 때까지 반복한다.
            current = stack.pop()
            if visited[current] == 0:
                visited[current] = 1
            for i in range(n):
                if visited[i] == 0 and computers[current][i] == 1:
                    # 현재 위치한 노드를 기준으로 연결되어 있고,
                    # 방문한 적이 없는 노드만 스택에 담는다.
                    stack.append(i)

    answer = 0
    # visited: 각 컴퓨터(노드)들이 연결된 상태를 확인하는 리스트
    visited = [0] * n

    i = 0
    # 아직 거치지 않은 노드가 있거나 index를 넘어서면 탐색 종료
    while (0 in visited) or i < n:
        if visited[i] == 0:
            dfs(i)
            answer += 1

        i += 1

    return answer


if __name__ == "__main__":
    test_cases = [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
    ]
    expected = [2, 1]
    for i in range(len(test_cases)):
        _n, _computers = test_cases[i]
        expect = expected[i]
        ans = solution(_n, _computers)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
