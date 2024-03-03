# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = head
        cur = head

        for _ in range(n):
            cur = cur.next

        if not cur:
            return head.next
        
        while cur.next:
            cur = cur.next
            pre = pre.next
        
        pre.next = pre.next.next

        # print(head)
        return head
