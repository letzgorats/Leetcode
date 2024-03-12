# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        answer = ListNode(0)
        answer.next = head
        prefix = 0
        d = {0:answer}

        while head:

            prefix += head.val
            d[prefix] = head
            head = head.next
        
        head = answer
        prefix = 0
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next
        
        return answer.next

