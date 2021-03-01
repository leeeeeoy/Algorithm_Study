"""
Programmers 43163. 단어 변환
url: https://programmers.co.kr/learn/courses/30/lessons/43163
writer: Harim Kang
Language: Python3
Date: 2021.02.27
Status: Success, Runtime: 640 ms, Memory Usage: 34252 KB
"""


def solution(begin, target, words):
    answer = 0

    def dfs(begin, target, words, visited, answer):
        stacks = [begin]
        while stacks:
            # 스택을 활용한 dfs 구현
            stack = stacks.pop()
            if stack == target:
                return answer
            for w in range(0, len(words)):
                # 조건 1. 한 개의 알파벳만 다른 경우
                if (
                    len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]])
                    == 1
                ):
                    if visited[w] != 0:
                        continue
                    visited[w] = 1
                    # stack에 추가
                    stacks.append(words[w])

            # depth +
            answer += 1

    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0
    visited = [0 for _ in words]
    answer = dfs(begin, target, words, visited, answer)

    return answer


if __name__ == "__main__":
    inputs = [
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
    ]
    expected = [4, 0]
    resp = []
    for begin, target, words in inputs:
        resp.append(solution(begin, target, words))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)