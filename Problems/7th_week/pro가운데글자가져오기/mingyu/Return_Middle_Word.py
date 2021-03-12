"""
Programmers. 가운데 글자 가져오기
url: https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
writer: Mingyu
Language: Python3
Date: 2021.03.02
Status: , Runtime:  ms, Memory Usage:  KB
"""


def solution(s):
    # 단어의 길이가 짝수라면
    if len(s) % 2 == 0:
        # s[x:y]는 인덱스 x이상 인덱스 y미만의 원소를 리턴한다. 그러므로
        # 가운데 문자 2개를 고르기 위해서는 단어 길이 / 2 - 1(배열의 인덱스는 0부터 시작하므로 -1을 해주는 것이다.)부터
        # 단어 길이 / 2 + 1(인덱스 y '미만'이기 때문에 y를 포함하기 위해 +1을 해준다)까지를 슬라이싱하여 return해주면 된다.
        return s[len(s) // 2 - 1: len(s) // 2 + 1]
    # 단어의 길이가 홀수라면
    else:
        # 단어의 중간을 return
        return s[len(s) // 2]


''' 주석 없느 코드

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1: len(s) // 2 + 1]
    else:
        return s[len(s) // 2]
'''
