"""
LeetCode 55. Jump Game
url: https://leetcode.com/problems/jump-game/
writer: Harim Kang
Language: Python3
Date: 2021.02.03
Status: Success, Runtime: 40 ms, Memory Usage: 14.1 MB
"""


class Solution:
    def canJump(self, nums):
        # 최대로 가능한 index를 저장하는 변수
        max_idx = 0

        # nums를 돌면서,
        for i in range(len(nums)):
            # 0이 아닌데, 최대를 넘어서면 False -> jump를 못한다는 뜻
            if i != 0 and max_idx < i:
                return False

            # jump 했을 때의 위치 계산
            jump = i + nums[i]
            # 최대 index 갱신
            if max_idx < jump:
                max_idx = jump
            # jump가 마지막 idx를 지나치면 무조건 True
            if jump >= len(nums) - 1:
                return True

        # 그 외는 모두 False
        return False


if __name__ == "__main__":
    inputs = [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [0, 2, 3], [0], [1, 0, 1, 0]]
    expected = [True, False, False, True, False]
    resp = []
    sol = Solution()
    for num in inputs:
        resp.append(sol.canJump(nums=num))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
