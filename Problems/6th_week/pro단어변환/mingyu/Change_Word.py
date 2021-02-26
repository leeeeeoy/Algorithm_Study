"""
Programmers. 단어 변환
url: https://programmers.co.kr/learn/courses/30/lessons/43163
writer: Mingyu
Language: Python3
Date: 2021.02.25
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(begin, target, words):
    # 타겟 단어가 words에 없으면 0을 return
    if target not in words:
        return 0

    # Depth
    answer = 0
    # 해당 단어를 방문했는지 여부를 체크할 dict
    visited = {i: 0 for i in words}
    # stack에 단어를 넣고 변환되는 단어를 찾을 것이다.
    # 시작 단어인 begin을 넣은 채로 시작
    stack = [begin]

    # BFS
    # stack이 빌 때까지
    while stack:
        # stack의 마지막을 체크할 단어로 설정
        check = stack.pop()

        # check가 target과 같다면 현재까지의 Depth에 타겟 단어가 있다는 것이다. Depth를 저장하고 있는 answer를 리턴
        if check == target:
            return answer

        # 각 단어와
        for word in words:
            # 그 단어의 알파벳을 하나씩 돌면서
            for i in range(len(word)):
                # word와 check를 한 단어씩 지우고 나머지가 일치한지 확인하기 위해
                # 둘 다 list로 설정 후 한 단어씩 0으로 마스킹한다.
                mask_word, mask_check = list(word), list(check)
                mask_word[i], mask_check[i] = 0, 0

                # 마스킹한 두 단어가 같을 경우(마스킹한 부분을 제외한 다른 알파벳이 일치하는 경우)
                if mask_word == mask_check:
                    # 해당 단어를 이미 방문하였다면 바로 다음 단어로 넘어간다
                    if visited[word]:
                        continue

                    # 방문하지 않았다면 방문했다는 표시인 1을 설정하고
                    visited[word] = 1
                    # 해당 단어를 stack에 추가. BFS를 돌리기 위함이다.
                    stack.append(word)
                    # for문을 탈출하여 다음 단어로 간다.
                    break

        # 한 단어를 바꿀 수 있는 계층을 다 돌았다면 Depth를 증가한다.
        answer += 1

    return answer


''' 주석 없는 코드

def solution(begin, target, words):   
    if target not in words:
        return 0

    answer = 0
    visited = {i: 0 for i in words}
    stack = [begin]

    while stack:
        check = stack.pop()

        if check == target:
            return answer

        for word in words:
            for i in range(len(word)):
                mask_word, mask_check = list(word), list(check)
                mask_word[i], mask_check[i] = 0, 0
                if mask_word == mask_check:
                    if visited[word]:
                        continue

                    visited[word] = 1
                    stack.append(word)
                    break

        answer += 1

    return answer
'''
