"""
LeetCode 100. Same Tree
url: https://leetcode.com/problems/same-tree/
writer: Harim Kang
Language: Python3
Date: 2021.01.28
Status: Success, Runtime: 40 ms, Memory Usage: 14.1 MB
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # None check
        # 둘다 None이면 같은거긴 하지..
        if p is None and q is None:
            return True

        # p 또는 q가 비어있을 경우
        if p is None or q is None:
            return False

        answer = False
        # 우선 자기 자신이 같아야함
        if p.val == q.val:
            # 그 다음엔 왼쪽 오른쪽이 같아야 된다.
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                answer = True

        return answer


if __name__ == "__main__":
    inputs = [
        [TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))],
        [TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))],
        [TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))],
    ]
    expected = [True, False, False]
    resp = []
    sol = Solution()
    for p, q in inputs:
        resp.append(sol.isSameTree(p=p, q=q))

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
