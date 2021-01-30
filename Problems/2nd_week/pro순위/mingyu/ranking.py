"""
Programmers. 순위
url: https://programmers.co.kr/learn/courses/30/lessons/49191
writer: Mingyu
Language: Python3
Date: 2021.01.22
Status: , Runtime:  ms, Memory Usage:  KB
"""

def solution(n, results):

    # 선수의 시작 번호는 1. 자꾸 n+1 쓰기 귀찮아서 length로 명명했다.
    length = n + 1

    # 중복 제거를 위해 내부 배열을 set으로 설정
    # 내부 배열 인자들에게 이김
    win_over = [set() for _ in range(length)]
    # 내부 배열 인자들에게 짐
    lose_to = [set() for _ in range(length)]

    # 승자와 패자를 각 리트스에 넣어준다.
    for A, B in results:
        win_over[A].add(B)
        lose_to[B].add(A)

    # 1. A가 B에게 이겼다면, A는 B가 이긴 모든 사람들에게 이긴 것과 같다.
    # 2. B가 A에게 졌다면, B는 A가 진 모든 사람들에게 진 것과 같다.
    for i in range(1, length):
        # lose_to[i]에 대해 w가 이겼다면
        for w in lose_to[i]:
            # i가 이긴 모든 사람들은 w가 이긴 것과 같다. 즉 승자의 배열에 이들을 추가한다.
            # update는 set에서 여러 값, 배열을 한번에 추가할 때 쓴다.
            win_over[w].update(win_over[i])

        # win_over[i]에 대해 l이 졌다면
        for l in win_over[i]:
            # i가 패배한 사람들은 l이 싸워도 패배한다. 즉 패자의 배열에 이들을 추가한다.
            lose_to[l].update(lose_to[i])

    # 순위를 확실히 알 수 있는 사람의 수
    answer = 0

    # 각 선수의 이긴 선수의 길이와 진 선수의 길이의 합이 전체 n에서 자기 자신을 뺸 n -1과 같다면 순위가 정확하게 체크된다.
    for i in range(1, length):
        if len(win_over[i]) + len(lose_to[i]) == n - 1:
            # 해당 조건을 통과했다면 순위를 확실히 알 수 있는 사람이므로 answer += 1
            answer += 1

    return answer




''' 주석 없는 코드
def solution(n, results):
    length = n + 1

    win_over = [set() for _ in range(length)]
    lose_to = [set() for _ in range(length)]

    for A, B in results:
        win_over[A].add(B)
        lose_to[B].add(A)

    for i in range(1, length):
        for w in lose_to[i]:
            win_over[w].update(win_over[i])

        for l in win_over[i]:
            lose_to[l].update(lose_to[i])

    answer = 0
    for i in range(1, length):
        if len(win_over[i]) + len(lose_to[i]) == n - 1:
            answer += 1

    return answer
'''