"""
LeetCode 92. 역순 연결 리스트 2
url: https://leetcode.com/problems/reverse-linked-list-ii/
writer: Mingyu
Language: Python3
Date: 2021.02.14
Status: , Runtime:  ms, Memory Usage:  KB
"""

# 리스트노드의 구조
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        # head가 비어있거나 m과 n이 같은 경우, 즉 변경할 부분이 없는 경우에는 head를 그대로 리턴한다
        if not head or m == n:
            return head

        # m부터 n까지의 숫자를 역순으로 재정렬할 리스트
        num = list()
        
        # 우선 head에 있는 val을 모두 받아서 그대로 num에 저장한다.
        while head:
            num.append(head.val)
            head = head.next

        # num의 m번째부터 n번째까지의 수를 역순으로 재정렬
        num[m-1:n] = reversed(num[m-1:n])
        
        # root와 num_linked_list를 따로 정의한 이유는 num_linked_list에서 노드의 추가 작업을 실시한 후
        # root 자체를 불러옴으로써 연결리스트 전체를 가져오기 위함이다. 
        # num_linked_list를 바로 쓰지 못하는 이유는 하단 for문에서 next를 반복하며 num_linked_list가 가리키는 위치가 맨 끝이 되어버리기 때문
        root = num_linked_list = ListNode(0)

        # num_linked_list에 num에 있는 숫자를 ListNode의 형태로 추가해준다
        # num_linked_list는 계속해서 next를 해주어 다음 노드를 가리킬 수 있도록 한다.
        for i in num:
            num_linked_list.next = ListNode(i)
            num_linked_list = num_linked_list.next
        
        # root를 리턴하면 ListNode(0), 즉 0도 같이 나오게 된다. 그러니 root의 next부터 리턴해주도록 한다.
        return root.next



''' 주석 없는 코드

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:            
        if not head or m == n:
            return head

        num = list()
        
        while head:
            num.append(head.val)
            head = head.next

        num[m-1:n] = reversed(num[m-1:n])
        
        root = num_linked_list = ListNode(0)

        for i in num:
            num_linked_list.next = ListNode(i)
            num_linked_list = num_linked_list.next
        
        return root.next
'''