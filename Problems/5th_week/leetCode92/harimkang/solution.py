"""
LeetCode 92. Reverse Linked List II
url: https://leetcode.com/problems/reverse-linked-list-ii/
writer: Harim Kang
Language: Python3
Date: 2021.02.09
Status: Success, Runtime: 28 ms, Memory Usage: 14.6 MB
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        val_list = []
        node = head
        val_list.append(node.val)
        while node.next is not None:
            node = node.next
            val_list.append(node.val)

        val_list = val_list[: m - 1] + val_list[m - 1 : n][::-1] + val_list[n:]

        temp = None
        while val_list:
            val = val_list.pop()
            if temp is None:
                temp = ListNode(val=val)
            else:
                temp = ListNode(val=val, next=temp)

        return temp


if __name__ == "__main__":
    inputs = [[ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4]]
    expected = [1, 4, 3, 2, 5]
    resp = []
    sol = Solution()
    for node, m, n in inputs:
        t = sol.reverseBetween(node, m, n)
        resp.append(t.val)
        while t.next:
            t = t.next
            resp.append(t.val)

    if expected == resp:
        print("PASSED")
    else:
        print("FAILED")
        print("Expected: ", expected)
        print("outputs :", resp)