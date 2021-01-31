"""
LeetCode 101. Symmetric Tree
url: https://leetcode.com/problems/symmetric-tree/
writer: Harim Kang
Language: Python3
Date: 2021.01.29
Status: Success, Runtime: 36 ms, Memory Usage: 14.5 MB
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def valueCheck(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        # 우선 자기 자신이 같아야함
        if left.val == right.val:
            return self.valueCheck(left.left, right.right) and self.valueCheck(
                left.right, right.left
            )

        return False

    def isSymmetric(self, root: TreeNode) -> bool:

        # None check
        # root가 None이면 일단 돌아가자
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        return self.valueCheck(root.left, root.right)


if __name__ == "__main__":
    inputs = [
        TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        ),
        TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))),
    ]
    expected = [True, False]
    resp = []
    sol = Solution()
    for root in inputs:
        ans = sol.isSymmetric(root=root)
        resp.append(ans)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)
