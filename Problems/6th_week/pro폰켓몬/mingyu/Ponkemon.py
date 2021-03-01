"""
Programmers. 폰켓몬
url: https://programmers.co.kr/learn/courses/30/lessons/1845
writer: Mingyu
Language: Python3
Date: 2021.02.26
Status: , Runtime:  ms, Memory Usage:  KB
"""
nums = [3, 3, 3, 2, 2, 2]


def solution(nums):
    answer = 0

    # 데려갈 수 있는 폰켓몬의 수
    gacha = len(nums) // 2
    # nums를 set으로 중복을 제거하고 다시 list로 만듦
    nums = list(set(nums))

    # 중복이 모두 제거되었으니, nums의 원소를 돌면서
    for _ in nums:
        # answer을 데려갈 수 있는 포켓몬의 최대치까지 올림.
        # 결국 최대치는 gacha와 같고, [1, 1, 1, 1]처럼 gacha 미만의 경우의 수가 나오는 경우를 판별하기 위함이다.
        if answer < gacha:
            answer += 1

    return answer


print(solution(nums))

''' 주석 없는 코드

def solution(nums):
    answer = 0

    gacha = len(nums)//2
    nums = list(set(nums))

    for _ in nums:
        if answer < gacha:
            answer += 1

    return answer
'''
