"""
LeetCode 55. 점프 게임
url: https://leetcode.com/problems/jump-game/
writer: Mingyu
Language: Python3
Date: 2021.02.02
Status: , Runtime:  ms, Memory Usage:  KB
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # 현재 위치에서 전진할 수 있는 칸의 수
        move_able = 0

        # 마지막 칸에 도착하면 성공한 것이므로 맨 마지막 원소는 0이어도 상관이 없다. 즉 확인할 필요가 없다는 뜻이다.
        # 맨 마지막 원소까지 도착하기 전에 M이 0이 된다면(더 이상 전진할 수 없다면) 성공할 수 없다는 뜻이다.
        for i in nums[:-1]:
            # i가 1 증가했기 때문에, M에서 전진할 수 있는 칸의 수는 -1을 해주어야 한다.
            # move_able 자체가 i의 이전 칸을 기준으로 설정되었기 때문이다.
            move_able = max(move_able-1, i)
            print(move_able, i)

            # 맨 마지막 원소에 도착하기 전에 M이 0이 된다면 불가능하다는 뜻이다.
            if move_able == 0:
                return False

        # 위의 for문을 통과했다면 nums의 끝에 도달할 수 있다는 뜻이다.
        return True


''' 주석 없는 코드

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        move_able = 0

        for i in nums[:-1]:
            move_able = max(move_able-1, i)
            print(move_able, i)

            if move_able == 0:
                return False

        return True
'''