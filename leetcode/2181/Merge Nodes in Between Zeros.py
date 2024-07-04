# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        current = dummy

        while head.next != None:

            value = 0
            while head.next.val != 0:
                value += head.next.val
                head = head.next

            if value != 0:
                current.next = ListNode(value)
                current = current.next
            # print(current)
            # print(dummy)
            head = head.next

        return dummy.next



