# iterative solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # Reverse the list
        prev, curr = None, head
        while curr :
            curr.next, prev, curr = prev, curr, curr.next
        
        curr, prev.next = prev.next, None

        while curr :
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp
        
        return prev


# recursive solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head : return None

        head.next = self.removeNodes(head.next)
        
        if head.next and head.val < head.next.val:
            return head.next
        
        return head
      
