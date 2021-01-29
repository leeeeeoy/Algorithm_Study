"""
LeetCode 101. 대칭 트리
url: https://leetcode.com/problems/symmetric-tree/
writer: Mingyu
Language: Python3
Date: 2021.01.28
Status: , Runtime:  ms, Memory Usage:  KB
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 루트 노드가 없다면 대칭은 맞다. 
        if not root:
            return True

        # 루트 노드의 좌 우 자식노드의 값을 스택에 저장
        stack = [(root.left, root.right)]

        # 덱이 빌 때까지
        while stack:
            # 좌 우 노드의 값을 받아서
            left, right = stack.pop()

            # 좌 우 노드가 값이 없다면 반대쪽 노드의 값도 확인해봐야 하므로 우선 넘어간다.
            if not left and not right:
                continue

            # 좌 우 노드 중 한 쪽만 값이 있다면 대칭이 되지 않는다. 그러므로 False
            if not left or not right:
                return False

            # 좌 우 노드의 값이 다르면 대칭이 되지 않는다.
            if left.val != right.val:
                return False
            
            # 좌측 노드의 좌측 주삭과 우측 노드의 우측 자식을 비교하기 위해 값을 넣는다.
            stack.append((left.left, right.right))

            # 좌측 노드의 우측 자식과 우측 노드의 좌측 자식을 비교하기 위해 값을 넣는다. 
            # 이 두 줄을 수행하면 트리가 거울 대칭형으로 형성되어 있는지 알 수 있다.
            stack.append((left.right, right.left))
        
        # 상기된 모든 조건을 통과했다면 거울대칭형 트리가 맞다.
        return True



''' 주석 없는 코드

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return True
'''