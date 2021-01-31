"""
LeetCode 100. 같은 트리
url: https://leetcode.com/problems/same-tree/
writer: Mingyu
Language: Python3
Date: 2021.01.28
Status: , Runtime:  ms, Memory Usage:  KB
"""
# 미리 정의된 이진트리 노드. 이미 정의되어 있으니 실제 코드에선 안 써도 된다.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 나 자신과 각  트리 노드 두 개를 인자로 받는다. bool타입으로 반환형을 설정.
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:      
        # p도 비어있고 q도 비어있으면 똑같은 트리다. 그러므로 True
        if not p and not q:
            return True
        
        # 둘 중 하나는 비어있는데 하나는 값이 있다는 것은 다른 트리라는 뜻이다. 
        if not p or not q:
            return False

        # 둘 다 값이 있을 때, 각 루트 노드가 가진 val 값이 같고 좌우 자식 노드들의 값이 전부 같으면 True가 리턴된다. 도중에 하나라도 다르면 False 리턴/
        return (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))



''' 주석 없는 코드
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:      
        if not p and not q:
            return True
        if not p or not q:
            return False

        return (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
'''