"""
LeetCode 819. 가장 평범한 단어
url: https://leetcode.com/problems/most-common-word/
writer: Mingyu
Language: Python3
Date: 2021.02.04
Status: , Runtime:  ms, Memory Usage:  KB
"""

# 정규표현식 사용을 위한 모듈
import re

# 동일 원소의 값과 개수를 파악할 수 있는 모듈
from collections import Counter

def mostCommonWord(paragraph, banned):
    
    # re.sub('[삭제할 단어 리스트]', '삭제한 단어를 치환할 단어', 해당 작업을 수행할 문자열)
    # 문제에서 " paragraph 문자, 공백 또는 구두점 기호로만 구성됨 !?',;. "라는 문구가 있는데, 처음에 !?',;. 만 제거했더니 오류가 났다.
    # 그래서 알파벳을 제외한 모든 단어를 없애기로 했다.
    # ^는 Not(부정)을 뜻하는 비트연산자이다. 즉 [^A-z]는 [A부터 z가 아니라면] 이라는 뜻이 된다
    # 대문자 A로 시작하고 소문자 z로 끝나는 이유는 아스키코드 상에서 대문자 알파벳이 먼저 나오고 그 다음에 소문자 알파벳이 나오기 때문이다. 
    # 즉 [A, B, C, ... , x, y, z] 만큼의 리스트를 받게 되는 것이다.
    paragraph = re.sub('[^A-z]', ' ', paragraph)

    # 위에서 알파벳이 아닌 것들은 처리했으나 아직 문자열 자체에서 대소문자를 구분하지는 않았다.
    # 대소문자 구분이 없으므로 전부 소문자로 처리하여 리스트로 받아온다.
    word_list = list(paragraph.lower().split())

    # 금지 문자 삭제
    for ban_word in banned:

        # remove는 기본적으로 한 번 수행한 후 종료된다. 
        # 때문에 같은 단어를 여러 번 지우기 위해서는 while문을 사용하여 더 이상 없을 때까지 지워주어야 한다.
        while ban_word in word_list:
            word_list.remove(ban_word)

    # Counter(검사할 리스트).most_common()은 리스트에서 가장 많이 나온 순으로 내림차순 배열되며 (['값', 개수])의 형태로 반환된다.
    # most_common(보이기 원하는 만큼의 수)를 통해 가장 많이 나온 것을 볓 번째 순위까지 나타낼지 정할 수 있다. 안 쓰면 모두 나타난다.
    # (['값', 개수])의 형태로 반환되므로 [0][0]을 통해 '값'만 가져오도록 하자
    common_word = Counter(word_list).most_common(1)[0][0]

    # 값을 리턴
    return common_word

''' 주석 없는 코드

import re
from collections import Counter

def mostCommonWord(paragraph, banned):
    paragraph = re.sub('[^A-z]', ' ', paragraph)
    word_list = list(paragraph.lower().split())
    for ban_word in banned:
        while ban_word in word_list:
            word_list.remove(ban_word)

    common_word = Counter(word_list).most_common(1)[0][0]
    return common_word
'''