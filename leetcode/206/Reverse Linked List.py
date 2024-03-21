# 1) iterative solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_list = None

        current = head

        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
    

        return new_list


# 2) recursive solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverseList(self, head,prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return prev
        
        temp = head.next
        head.next = prev
        return self.reverseList(temp,head)
